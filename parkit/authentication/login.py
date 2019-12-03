import pyrebase
from flask import *
app = Flask(__name__)


from config import firebase as fbaseProject

firebase = pyrebase.initialize_app(fbaseProject.FIREBASE_CONFIG)
auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])
def basic():
	unsuccessful = 'Please check your credentials'
	successful = 'Login successful'
	if request.method == 'POST':
		email = request.form['name']
		password = request.form['pass']
		try:
			auth.sign_in_with_email_and_password(email, password)
			return render_template('login.html', s=successful)
		except:
			return render_template('login.html', us=unsuccessful)

	return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=4000)


print (fbaseProject.projectname)




