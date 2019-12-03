import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("parkit-zachandfaz-firebase-adminsdk-30ltr-452668633e.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

lot_ref = db.collection(u'test_lot_0')
docs = lot_ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))

lot_ref.document(u'0').set({u'reserved' : False, u'taken' : False})
time.sleep(2)

doc_num = 0

doc_ref = db.collection(u'test_lot_0').document(str(doc_num))

try:
    doc = doc_ref.get()
    print(str(doc_num)+': {}'.format(doc.to_dict()))
except:
    print(u'No such document')

# try:
#     doc = lot_ref.get()
#     print(u'Document data: {}'.format(doc.to_dict()))
# except:
#     print(u'No such document')
