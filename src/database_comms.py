import firebase_admin
import config
from firebase_admin import credentials
from firebase_admin import db

# Setting up credentials and initializing database connection
cred = credentials.Certificate(config.credentials_path)
firebase_admin.initialize_app(cred, {'databaseURL': config.databaseURL})

# Getting reference to the database
ref = db.reference('lot_data')

################################################################################
# Function Name: get_document_data
#   Description: Get data from database entry in the lot.
#                Data is returned as a dictionary
################################################################################
def get_document_data(doc_name):
    item = {}

    spot_ref = ref.child(doc_name)
    try:
        item = spot_ref.get()
    except:
        print('No such item!')

    return(item)

################################################################################
# Function Name: set_document_data
#   Description: Writes data back to the database at the specified entry.
#                Data passed is a dictionary.
################################################################################
def set_document_data(doc_name, data):
    item = ref.get()
    item[doc_name] = data
    try:
        ref.update(item)
    except:
        print("Failed to write data.")

def set_document_field(field_name, data):
    spot_ref = ref.child(config.spot_num)
    spot_data = spot_ref.get()
    spot_data[field_name] = data
    try:
        spot_ref.update(spot_data)
    except:
        print("Field data failed to write.")

################################################################################
# Function Name: get_lot_data
#   Description: Gets the data for the whole lot.
################################################################################
def get_lot_data():
    return(ref.get())
