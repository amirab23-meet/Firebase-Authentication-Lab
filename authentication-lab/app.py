from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey": "AIzaSyBwMLMG6TlrTRWvrImpn7kgKxVEF3ExJRI",
  "authDomain": "cs-amir-gp-f.firebaseapp.com",
  "projectId": "cs-amir-gp-f",
  "storageBucket": "cs-amir-gp-f.appspot.com",
  "messagingSenderId": "531475169244",
  "appId": "1:531475169244:web:06192ca20d569bc89a5919",
  "measurementId": "G-SL0HLVBCQG",
  "databaseURL":"https://cs-amir-gp-f-default-rtdb.europe-west1.firebasedatabase.app/"


  
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()




app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if  request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] == auth.sign_in_with_email_and_password(email, password)

            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
                
            return redirect(url_for('home'))
       except:
            error = "Authentication failed"
    return render_template("signup.html")





@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)