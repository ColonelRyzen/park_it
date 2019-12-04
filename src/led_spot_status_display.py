import time
import config
import led_ctrl
import database_comms

def update_led_status():
    led_color = "white"
    while True:
        # Get status of spot and set led color accordingly
        spot_data = database_comms.get_document_data(config.spot_num)
        time.sleep(2)

        led_color = spot_data["led_color"]
        print(led_color)
        if led_color == "white":
            led_ctrl.whiteOff()
            led_ctrl.whiteOn()
        elif led_color == "green":
            led_ctrl.whiteOff()
            led_ctrl.greenOn()
        elif led_color == "red":
            led_ctrl.whiteOff()
            led_ctrl.redOn()
        elif led_color == "yellow":
            led_ctrl.whiteOff()
            led_ctrl.yellowOn()

        spot_status = spot_data["taken"]
        reservation_status = spot_data["reserved"]
        if reservation_status == True and spot_status == False:
            spot_data["led_color"] = "yellow"
            database_comms.set_document_data(config.spot_num, spot_data)
        elif reservation_status == False and spot_status == True:
            spot_data["led_color"] = "red"
            database_comms.set_document_data(config.spot_num, spot_data)
        else:
            spot_data["led_color"] = "green"
            database_comms.set_document_data(config.spot_num, spot_data)

def main():
    update_led_status()

main()

# def set_led_color():
#     while True:
#         spot_data = database_comms.get_document_data(config.spot_database_name, config.spot_num)
#         led_color = spot_data["led_color"]
#
#         if led_color == "white":
#             led_ctrl.whiteOff()
#             led_ctrl.whiteOn()
#         elif led_color == "green":
#             led_ctrl.whiteOff()
#             led_ctrl.greenOn()
#         elif led_color == "red":
#             led_ctrl.whiteOff()
#             led_ctrl.redOn()
#         elif led_color == "yellow":
#             led_ctrl.whiteOff()
#             led_ctrl.yellowOn()
