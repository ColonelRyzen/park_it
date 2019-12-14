import firebase_admin
import config
from firebase_admin import credentials
from firebase_admin import db

#def get_database_reference():
cred = credentials.Certificate(config.credentials_path)
firebase_admin.initialize_app(cred, {'databaseURL': config.databaseURL})

ref = db.reference('lot_data')
#    return(lot_ref)

def get_document_data(doc_name):
 #   lot_ref = get_database_reference()
    #doc_ref = lot_ref.document(doc_name)
    #try:
        #doc = doc_ref.get()
    #except:
        #print(u'No such document!')

    #return(doc.to_dict())
    item = {}

    spot_ref = ref.child(doc_name)
    try:
        item = spot_ref.get()
    except:
        print('No such item!')
    
    return(item)

# All fields of the document must be filled in when writing to a document
def set_document_data(doc_name, data):
  #  lot_ref = get_database_reference()
    #lot_ref.document(doc_name).set(data_dict)
    item_ref = ref.child(doc_name)
    item = item_ref.get()

    #if type(item) is dict:
       # item[doc_name] = data
        #try:
        #    item_ref.update(item)
        #except:
            #print("Failed to write dict data.")
    #else:
    item = ref.get()
    item[doc_name] = data
    try:
        ref.update(item)
    except:
        print("Failed to write data.")
