import config
import database_comms
import time

def count_spots_in_lot():
    lot_data = database_comms.get_lot_data()
    num_spots_in_lot = len(lot_data) - 1
    return(num_spots_in_lot)

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

