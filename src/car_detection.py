import time
import config
import database_comms
import ultra_sonic_ctrl
import update_free_spot_count

def detect_car():
    car_detection = False
    in_range_count = 0
    num_free_spots = config.num_spots_in_lot

    # Check for car every second.
    # After car_detection_threshold seconds, trigger a detection
    while True:
        update_free_spot_count.update_free_spot_count()
        in_range_bool = ultra_sonic_ctrl.object_in_range(config.min_distance_cm, config.max_distance_cm)
        num_free_spots_db = database_comms.get_document_data(config.num_free_spots)
        time.sleep(1)
        #print("in_range_count: ", in_range_count)
        # Check if the car has been parked for car_detection_threshold seconds
        # There is a 2 second delay between the car leaving and the car no longer being detected
        if in_range_count == config.car_detection_threshold:
            car_detection = True
            doc_data = database_comms.get_document_data(config.spot_num)
            print("True Case: ", doc_data["taken"])
            # lot_data = database_comms.get_document_data(config.lot_database_name, config.lot_id)
            if doc_data["taken"] == False:
                doc_data["taken"] = car_detection
                print("Writing that the spoty is taken.")
                database_comms.set_document_data(config.spot_num, doc_data)
                # lot_data["num_free_spots"] = lot_data["num_free_spots"] - 1
                # database_comms.set_document_data(config.lot_database_name, config.lot_id, lot_data)

        elif in_range_count <= config.car_detection_threshold - config.car_stop_detecting_delay:
            car_detection = False
            doc_data = database_comms.get_document_data(config.spot_num)
            print("False Case: ", doc_data["taken"])
            # lot_data = database_comms.get_document_data(config.lot_database_name, config.lot_id)
            if doc_data["taken"] == True:
                doc_data["taken"] = car_detection
                print("Writing that spot is free.")
                database_comms.set_document_data(config.spot_num, doc_data)
                # lot_data["num_free_spots"] = lot_data["num_free_spots"] + 1
                # database_comms.set_document_data(config.lot_database_name, config.lot_id, lot_data)

        print("bool: ",in_range_bool)
        print("count: ",in_range_count)
        print("\n\n\n")
        if in_range_bool == True and in_range_count < config.car_detection_threshold:
            in_range_count += 1
        if in_range_bool == False and in_range_count > 0:
            in_range_count -= 1

def main():
    detect_car()

main()
