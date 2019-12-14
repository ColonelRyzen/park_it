import config
import seven_segment_ctrl
import database_comms
import time

def update_sev_seg():
    sev_seg_value = config.max_num_spots
    while True:
        spot_data = database_comms.get_document_data(config.num_free_spots)
        time.sleep(2)

        #print("num_free_spots: ", spot_data["num_free_spots"])
        num_free_spots = spot_data
        print(num_free_spots)
        if num_free_spots == 0:
            seven_segment_ctrl.zero()
        elif num_free_spots == 1:
            seven_segment_ctrl.one()
        elif num_free_spots == 2:
            seven_segment_ctrl.two()
        elif num_free_spots == 3:
            seven_segment_ctrl.three()
        elif num_free_spots == 4:
            seven_segment_ctrl.four()
        elif num_free_spots == 5:
            seven_segment_ctrl.five()
        elif num_free_spots == 6:
            seven_segment_ctrl.six()
        elif num_free_spots == 7:
            seven_segment_ctrl.seven()
        elif num_free_spots == 8:
            seven_segment_ctrl.eight()
        elif num_free_spots == 9:
            seven_segment_ctrl.nine()

def main():
    update_sev_seg()

main()
