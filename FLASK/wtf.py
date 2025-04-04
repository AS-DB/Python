from flask_wtf import FlaskForm  
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, Email  

class ContactForm(FlaskForm):
    name = StringField("Name of Student", [DataRequired("Please enter your name.")])
    Gender = RadioField("Gender", choices=[('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField('Address')
    email = StringField("Email", validators=[DataRequired("Please enter your email address."), Email("Please enter a valid email address.")])
    Age = IntegerField("Age")
    language = SelectField('Language', choices=[('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField('Send')
