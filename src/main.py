import config
import time
import database_comms
import car_detection
import led_spot_status_display
import seven_segment_display
from multiprocessing import Process


if __name__ == '__main__':
    p0 = Process(target=car_detection.detect_car())
    p1 = Process(target=led_spot_status_display.update_led_status())
    p2 = Process(target=seven_segment_display.update_sev_seg())
    p0.start()
    p1.start()
    p2.start()
    p0.join()
    p1.join()
    p2.join()
