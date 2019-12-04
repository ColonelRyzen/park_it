import firebase_admin
import config
from firebase_admin import credentials
from firebase_admin import firestore

def get_database_reference():
    cred = credentials.Certificate(config.credentials_path)
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    lot_ref = db.collection(config.spot_database_name)
    return(lot_ref)

def get_document_data(doc_name):
    lot_ref = get_database_reference()
    doc_ref = lot_ref.document(doc_name)
    try:
        doc = doc_ref.get()
    except:
        print(u'No such document!')

    return(doc.to_dict())

# All fields of the document must be filled in when writing to a document
def set_document_data(doc_name, data_dict):
    lot_ref = get_database_reference(database_name)
    lot_ref.document(doc_name).set(data_dict)
