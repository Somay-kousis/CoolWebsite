from flask import Flask, render_template, url_for, request, make_response, redirect, render_template_string, session, jsonify
import firebase_admin
from firebase_admin import db, credentials

app = Flask(__name__)
app.secret_key = "hidden_key_you_can't_crack"
cred = credentials.Certificate("new.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://newbag-ee944-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/welcomeUser", methods=["POST", "GET"])
def welcomeUser():
    if request.method == "POST":
        username = request.form.get("Username", "").strip()
        password = request.form.get("Password", "").strip()
        if not username or not password:
            return "The username and password can't be empty :)", 400
        response = make_response(redirect("/welcomeUser"))
        response.set_cookie("Username", username, max_age=60*60*24)
        session["username"] = username
        return response
    return render_template("hat.html")

@app.route("/yourPurchases", methods=["GET"])
def yourPurchases():
    return render_template("purchases.html")

@app.route("/ContactUs", methods=["GET"])
def ContactUs():
    return render_template("contactus.html")

@app.route("/features", methods=['GET'])
def showFeatures():
    response = make_response(render_template("features.html"))
    return response
if __name__ == "__main__":
    app.run(debug=True)