import config
import database_comms
import time

################################################################################
# Function Name: count_spots_in_lot
#   Description: Checks the number of elements in a dictionary of the database data.
#                The length minus the 'num_free_spots' entry is the number of spots in the lot
################################################################################
def count_spots_in_lot():
    lot_data = database_comms.get_lot_data()
    num_spots_in_lot = len(lot_data) - 1
    return(num_spots_in_lot)

################################################################################
# Function Name: update_free_spot_count
#   Description: Loops through the spot entries in the databse and checks the
#                'taken' flag. The number of free spots is determined by subtracting
#                one from total number of spots in lot for each true value.
################################################################################
def update_free_spot_count():
    num_spots_in_lot = count_spots_in_lot()
    num_free_spots = num_spots_in_lot
    for spot_idx in range(0, num_spots_in_lot):
        spot_data = database_comms.get_document_data(str(spot_idx))
        if spot_data['taken'] == True:
            if num_free_spots > 0:
                num_free_spots -= 1
    db_num_free_spots = database_comms.get_document_data(config.num_free_spots)
    #print("free spots: ", type(db_num_free_spots))
    db_num_free_spots = num_free_spots
    database_comms.set_document_data(config.num_free_spots, db_num_free_spots)
    db_num_free_spots = database_comms.get_document_data(config.num_free_spots)
    print(db_num_free_spots)

    return(db_num_free_spots)
