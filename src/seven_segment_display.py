import config
# import seven_segment_ctrl
import database_comms
import time

def update_sev_seg():
    sev_seg_value = config.max_num_spots
    while True:
        spot_data = database_comms.get_document_data(config.spot_database_name, config.lot_id)
        time.sleep(2)

        print(lot_data)

        print("num_free_spots: ", spot_data["num_free_spots"])
        num_free_spots = lot_data["num_free_spots"]
        if num_free_spots == 0:
            seven_segment.zero()
        elif num_free_spots == 1:
            seven_segment.one()
        elif num_free_spots == 2:
            seven_segment.two()
        elif num_free_spots == 3:
            seven_segment.three()
        elif num_free_spots == 4:
            seven_segment.four()
        elif num_free_spots == 5:
            seven_segment.five()
        elif num_free_spots == 6:
            seven_segment.six()
        elif num_free_spots == 7:
            seven_segment.seven()
        elif num_free_spots == 8:
            seven_segment.eight()
        elif num_free_spots == 9:
            seven_segment.nine()

def main():
    update_sev_seg()

main()
