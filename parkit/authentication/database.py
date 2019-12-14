import pyrebase
import json

from config import firebase as fbaseProject
firebase = pyrebase.initialize_app(fbaseProject.FIREBASE_CONFIG)
db = firebase.database()
from flask import *
app = Flask(__name__)

class customer_info:
    name = ""
    dob = ""
    make = ""
    model = ""
    year = ""
    plate = ""

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        if request.form['submit'] == 'add':
            
            customer = customer_info()
            customer.name = request.form['name']
            customer.dob = request.form['dob']
            customer.make = request.form['make']
            customer.model = request.form['model']
            customer.year = request.form['year']
            customer.plate = request.form['plate']

            CUSTOMER_INFO = {
                "name": customer.name,
                "dob": customer.dob,
                "make": customer.make,
                "year": customer.model,
                "model": customer.year,
                "plate": customer.plate
            }

            db.child("car_info").push(CUSTOMER_INFO)
            todo = db.child("car_info").get()
            to = todo.val()
            return render_template('parkingspot.html', t=to.values())
        elif request.form['submit'] == 'delete':
            db.child("car_info").remove()
        return render_template('parkingspot.html')
    return render_template('parkingspot.html')

if __name__ == '__main__':
    app.run(debug=True)