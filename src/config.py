# HW pinouts
## RGB LED pins
led_red_pin = 11
led_green_pin = 13
led_blue_pin = 15

## Ultra Sonic Pins
ultra_sonic_trig = 16
ultra_sonic_echo = 18

## Seven Segment pins
sev_seg_a_pin = 10
sev_seg_b_pin = 9
sev_seg_c_pin = 11
sev_seg_d_pin = 0
sev_seg_e_pin = 5
sev_seg_f_pin = 6
sev_seg_g_pin = 13

#Car Detection Settings
min_distance_cm = 20
max_distance_cm = 150
car_detection_threshold = 5
car_stop_detecting_delay = 2
num_spots_in_lot = 1

# spot Database config
spot_database_name = "test_lot_0"
credentials_path = "parkit-zachandfaz-firebase-adminsdk-30ltr-452668633e.json"
databaseURL = "https://parkit-zachandfaz.firebaseio.com/"
spot_num = "0"
num_free_spots = "num_free_spots"

# Lots database config
lot_database_name = "lots"
max_num_spots = 2
lot_id = 0
