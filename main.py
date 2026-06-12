from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import StringField, EmailField, TelField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditor, CKEditorField
from bs4 import BeautifulSoup
import requests
import os

app = Flask(__name__)
ckeditor = CKEditor(app)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
EMAIL = "catalystengine27@gmail.com"
PASSWORD = os.environ.get("PASSWORD")

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    phone_no = TelField("Phone Number (Optional)")
    message = TextAreaField("Your Message", validators=[DataRequired()])
    submit = SubmitField()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pricing")
def pricing_plans():
    return render_template("pricing.html")

@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    form = ContactForm()
    if form.validate_on_submit():
        clean_message = BeautifulSoup(form.message.data, "html.parser").get_text()
        webhook_url = "https://discordapp.com/api/webhooks/1514237780757053500/lpaQIwMxLGMYp78z9dGoKI58_1l9-Gi8cIaj4ThkSLHtSUOlsHMvlH8TsWxA3EZ0CCoS"
        payload = {
            "content": f"🚀 **New Lead!**\n**Name:** {form.name.data}\n**Email:** {form.email.data}\n**Phone Number: {form.phone_no.data}**\n**Message:** {clean_message}"
        }
        requests.post(webhook_url, json=payload)
    return render_template("contact.html", form=form)

@app.route("/test")
def test_page():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True)