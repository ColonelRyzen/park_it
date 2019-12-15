import config
import database_comms
import time
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import cv2


def read_qr_codes():
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", type=str, default="qr_code.csv", help="path to output CSV file containg QR codes")
    args = vars(ap.parse_args())

    print("[INFO] starting video stream...")
    vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)

    csv = open(args["output"], "w")
    found = set()

    correct_car_in_reserved_spot = True

    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=400)

        qr_codes = pyzbar.decode(frame)
        for qrcode in qr_codes:
            (x,y,w,h) = qrcode.rect
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)

            qrcodeData = qrcode.data.decode("utf-8")
            qrcodeType = qrcode.type

            text = "{} ({})".format(qrcodeData, qrcodeType)
            cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            csv.write("{},{}\n".format(datetime.datetime.now(), qrcodeData))
            csv.flush()
            found.add(qrcodeData)
            print("I found the QR Code. QR code text: ",qrcodeData)

            # Read reserved status and user ID of spot
            spot_data = database_comms.get_document_data(config.spot_num)
            if spot_data['reserved'] == True:
                if spot_data['user_id'] == qrdcodeData:
                    correct_car_in_reserved_spot = True
                    print("Correct car is spot.")
                else:
                    correct_car_in_reserved_spot = False
                    print("Wrong car in spot.")

                spot_data['correct_car'] = correct_car_in_reserved_spot
                database_comms.set_document_data(config.spot_num, spot_data)

        cv2.imshow("QR Code Scanner", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        time.sleep(2)

    print("[INFO] cleaning up...")
    csv.close()
    cv2.destroyAllWindows()
    vs.stop()

    return(correct_car_in_reserved_spot)
