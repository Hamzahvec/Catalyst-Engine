from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, EmailField, TelField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditor, CKEditorField

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    phone_no = TelField("Phone Number (Optional)")
    message = CKEditorField("Your Message", validators=[DataRequired()])
    submit = SubmitField()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pricing")
def pricing_plans():
    return render_template("pricing.html")

@app.route("/contact")
def contact_page():
    form = ContactForm()
    return render_template("contact.html", form=form)

@app.route("/test")
def test_page():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True)