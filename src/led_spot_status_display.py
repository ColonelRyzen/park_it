import time
import config
import led_ctrl
import database_comms

################################################################################
# Function Name: update_led_status
#   Description: Changes the LED color based on the 'led_color' field in the spot
#                entry. Also, checkes the values of 'taken' and 'reserved' and sets
#                the led_color appropriately. This check and update happens once
#                every 2 seconds.
################################################################################
def update_led_status():
    led_color = "white"
    while True:
        # Get the data for the spot entry
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

        # Get the values of 'taken' and 'reserved'
        spot_status = spot_data["taken"]
        reservation_status = spot_data["reserved"]
        # Set the 'led_color' value based on the values of 'taken' and 'reserved'
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
