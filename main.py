#Portfolio Website
#Design your website

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap4
import os
import smtplib



PEOPLE_FOLDER = os.path.join('static/images')

OWN_EMAIL = "magdauchman93@gmail.com"
OWN_PASSWORD = "fivrhsffyjgcqzzp"


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
Bootstrap4(app)

@app.route('/')
def home():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'my_picture.jpg')
    return render_template("index.html", user_image=full_filename)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route('/projects')
def projects():
    return render_template("my_project.html")

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    #Runt he app in debug mode to auto-reload
    app.run(debug=True)
