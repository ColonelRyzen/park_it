import pyrebase
from flask import *
import json

from authentication import firebase_config as fbaseProject
from config.objects.user import UserInfo

app = Flask(__name__)

firebase = pyrebase.initialize_app(fbaseProject.FIREBASE_CONFIG)
auth = firebase.auth()
db = firebase.database()


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/signup',methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            aauth.create_user_with_email_and_password(email, password)
            return redirect(url_for('login'))
        except:
            return render_template('signup.html', us=unsuccessful)

        

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def home():
    unsuccessful = 'Please check your credentials'
    successful = 'Login successful'
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('parkingspot'))
        except:
            return render_template('login.html', us=unsuccessful)

    return render_template('login.html')

@app.route('/parkingspot', methods=['GET', 'POST'])
def parkingspot():
    if request.method == 'POST':
        if request.form['submit'] == 'add':


            userInfo = UserInfo(request.form['firstname'],request.form['lastname'], 
                                request.form['dob'],False,request.form['make'],request.form['model'],
                                request.form['year'],request.form['color'],request.form['vin'],
                                request.form['plate'])

            db.child("car_info").push(userInfo.toDictionary())
            todo = db.child("car_info").get()
            to = todo.val()
            return render_template('parkingspot.html', t=to.values())
        elif request.form['submit'] == 'delete':
            db.child("car_info").remove()
        return render_template('parkingspot.html')

    return render_template('parkingspot.html')

@app.route('/availablespots', methods=['GET', 'POST'])
def availablespots():
    
    todo = db.child("lot_data").get()
    to = todo.val()
    return render_template('availablespots.html', t=to.values())



if __name__ == "__main__":
    app.run(debug=True)