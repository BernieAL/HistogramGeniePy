from flask import Flask,url_for,render_template,redirect,request,session
from datetime import timedelta


app = Flask(__name__)
app.secret_key="SomeString"
app.permanent_session_lifetime = timedelta(days=5)

# url_for('static', filename='style.css')

@app.route('/')
def index():
    return render_template("base.html")


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        
        session.permanent = True

        #request.form comes in as a dictionary, we can access each form object using a key
        #the key must be the name that was used for the field in the form
        user = request.form["name"]
        email = request.form["email"]
        session["user"] = user
        session["email"] = email
        return redirect(url_for("user",user=user,email=email))

    else:

        #if user exists in session, redirect to user page - to avoid logging in again
        if "user" in session:
            return redirect(url_for("user"))    
        return render_template("login.html")

@app.route("/<user><email>")
def user(user,email):
    #checking if user is logged in, if they are get their data from the session object
    if "user" in session:
        user = session["user"]  
        email = session["email"]
        return f"<h1>{user} {email}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user",None)
    session.pop("email",None)
    return redirect(url_for("login"))



# UNCOMMENT TO RUN
# if __name__ == '__main__':
# 		app.run(debug=True)
	


