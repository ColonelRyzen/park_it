import config
import database_comms
import time
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import cv2

################################################################################
# Function Name: read_qr_codes
#   Description: Attempts to read a QR code in a frame of video every 2 seconds.
#                If a code is detected and the 'reserved' field is true then the
#                data in the qr code is compared the the value of the 'user_id'
#                field in the spot entry.
################################################################################
def read_qr_codes():
    # Setup a csv file for logging the data from the QR codes
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", type=str, default="qr_code.csv", help="path to output CSV file containg QR codes")
    args = vars(ap.parse_args())

    # Setup the video stream from the camera
    print("[INFO] starting video stream...")
    vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)

    csv = open(args["output"], "w")
    found = set()

    correct_car_in_reserved_spot = True

    # Loop that gets a new frame every 2 seconds
    while True:
        frame = vs.read()
        #frame = imutils.resize(frame, width=400)

        qr_codes = pyzbar.decode(frame)
        # loop through all detected QR codes in the frame
        for qrcode in qr_codes:
            (x,y,w,h) = qrcode.rect
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)

            # Get the data from the current QR code
            qrcodeData = qrcode.data.decode("utf-8")
            qrcodeType = qrcode.type

            text = "{} ({})".format(qrcodeData, qrcodeType)
            cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            # Write the data with the date and time to the csv file
            csv.write("{},{}\n".format(datetime.datetime.now(), qrcodeData))
            csv.flush()
            found.add(qrcodeData)
            print("I found the QR Code. QR code text: ",qrcodeData)

            # Get the spot data entry from the database
            spot_data = database_comms.get_document_data(config.spot_num)
            print(spot_data['user_id'])
            print(type(spot_data['user_id']))

            # Check if the spot is reserved and if the QR code data matches the 'user_id' value
            if spot_data['reserved'] == True:
                if spot_data['user_id'] == qrcodeData:
                    correct_car_in_reserved_spot = True
                    print("Correct car is spot.")

                    # If the 'correct_car' field is already true, don't write to the databse
                    if spot_data['correct_car'] == False:
                        spot_data['correct_car'] = correct_car_in_reserved_spot
                        database_comms.set_document_data(config.spot_num, spot_data)
                else:
                    correct_car_in_reserved_spot = False
                    print("Wrong car in spot.")

                    # if the 'correct_car' field is already false, don't write to the database
                    if spot_data['correct_car'] == True:
                        spot_data['correct_car'] = correct_car_in_reserved_spot
                        database_comms.set_document_data(config.spot_num, spot_data)

        # In Raspberry Pi desktop show the video frame
        cv2.imshow("QR Code Scanner", frame)

        # Check for the letter 'q' to be pressed to quit the loop.
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        time.sleep(1)

    print("[INFO] cleaning up...")
    csv.close()
    cv2.destroyAllWindows()
    vs.stop()

    return(correct_car_in_reserved_spot)
read_qr_codes()
