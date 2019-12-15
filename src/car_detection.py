import time
import config
import database_comms
import ultra_sonic_ctrl
import update_free_spot_count

####################################################################################################################
# Function Name: detect_car
#   Description: Uses the ultra sonic sensor to detect if a car is within a specified distance (in config.py)
#                Runs in a continuous loop checking for a car every second. If a car is detected and it previously
#                wasn't detected, the change is written to the database. If the car was already detected then
#                there is no write to the databse.
####################################################################################################################
def detect_car():
    car_detection = False
    in_range_count = 0
    num_free_spots = update_free_spot_count.count_spots_in_lot()

    # Check for car every second.
    # After car_detection_threshold seconds, trigger a detection
    while True:
        update_free_spot_count.update_free_spot_count()
        in_range_bool = ultra_sonic_ctrl.object_in_range(config.min_distance_cm, config.max_distance_cm)
        num_free_spots_db = database_comms.get_document_data(config.num_free_spots)
        time.sleep(1)

        # Check if the car has been parked for car_detection_threshold seconds
        # There is a 2 second delay between the car leaving and the car no longer being detected
        if in_range_count == config.car_detection_threshold:
            car_detection = True
            doc_data = database_comms.get_document_data(config.spot_num)

            # Check if spot has been previously taken
            # If not, write that it is taken to the database, otherwise do nothing.
            if doc_data["taken"] == False:
                doc_data["taken"] = car_detection
                print("Writing that the spot is taken.")
                database_comms.set_document_data(config.spot_num, doc_data)

        # If the car leaves and is not detected for 'car_stop_detecting_delay' seconds then the spot is free.
        elif in_range_count <= config.car_detection_threshold - config.car_stop_detecting_delay:
            car_detection = False
            doc_data = database_comms.get_document_data(config.spot_num)

            # If the spot is taken then write to the database that it is not.
            if doc_data["taken"] == True:
                doc_data["taken"] = car_detection
                print("Writing that spot is free.")
                database_comms.set_document_data(config.spot_num, doc_data)

        # the count that the detection threshold is based on.
        print("count: ",in_range_count)
        print("\n\n\n")
        # Detection threshold counter logic
        if in_range_bool == True and in_range_count < config.car_detection_threshold:
            in_range_count += 1
        if in_range_bool == False and in_range_count > 0:
            in_range_count -= 1

def main():
    detect_car()

main()
