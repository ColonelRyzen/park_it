import time
import config
import database_comms
import ultra_sonic_ctrl

def detect_car():
    car_detection = False
    in_range_count = 0

    # Check for car every second.
    # After car_detection_threshold seconds, trigger a detection
    while True:
        in_range_bool = ultra_sonic_ctrl.object_in_range(config.min_distance_cm, config.max_distance_cm)
        sleep(1)
        # Check if the car has been parked for car_detection_threshold seconds
        # There is a 2 second delay between the car leaving and the car no longer being detected
        if in_range_count == config.car_detection_threshold:
            car_detection = True
            doc_data = database_comms.get_document_data(config.spot_database_name, config.spot_num)
            lot_data = database_comms.get_document_data(config.lot_database_name, config.lot_id)
            if doc_data["taken"] == False:
                doc_data["taken"] = True
                database_comms.set_document_data(config.spot_database_name, config.spot_num, doc_data)
                lot_data["num_free_spots"] = lot_data["num_free_spots"] - 1
                database_comms.set_document_data(config.lot_database_name, config.lot_id, lot_data)
        elif in_range_count == config.car_detection_threshold - config.car_stop_detecting_delay:
            car_detection = False
            doc_data = database.get_document_data(config.spot_database_name, config.spot_num)
            lot_data = database_comms.get_document_data(config.lot_database_name, config.lot_id)
            if doc_data["taken"] == True:
                doc_data["taken"] = False
                database_comms.set_document_data(config.spot_database_name, config.spot_num, doc_data)
                lot_data["num_free_spots"] = lot_data["num_free_spots"] + 1
                database_comms.set_document_data(config.lot_database_name, config.lot_id, lot_data)
        if in_range_bool == True and in_range_count < config.car_detection_threshold:
            in_range_count += 1
        elif in_range_count == False:
            in_range_count -= 1
