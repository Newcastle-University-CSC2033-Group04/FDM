import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

class RegisterForm(FlaskForm):
    email = StringField()
    username = StringField()
    password = PasswordField()
    confirm_password = PasswordField()
    firstname = StringField()
    lastname = StringField()
    submit = SubmitField()

# Function used to exclude certain characters from user inputs
'''def character_check(form, field):
    excluded_chars = "*?!'^+%&/()=}][{$#@<>"
    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(
                f"Character {char} is not allowed.")


# Validators lists all the types of inputs required for the submit
class RegisterForm(FlaskForm):  # register form containing all the input fields
    username = StringField(validators=[DataRequired(), character_check])
    email = StringField(validators=[DataRequired(), Email(message='Invalid email address')])
    firstname = StringField(validators=[DataRequired(), character_check])
    lastname = StringField(validators=[DataRequired(), character_check])
    password = PasswordField(validators=[DataRequired(),
                                         Length(min=6, max=12,
                                                message='Password must be between 6 and 12 characters in length.')])
    confirm_password = PasswordField(
        validators=[DataRequired(), EqualTo('password', message='Both password fields must be equal!')])
    submit = SubmitField()

    # Function to validate password input contains certain characters
    def validate_password(self, password):
        pa = re.compile(r'(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@<>?/.,"£$%^&=*():;+{}|_-])')
        if not pa.match(self.password.data):
            raise ValidationError("Password must contain at least: 1 digit, 1 special character,"
                                  " 1 lowercase and 1 uppercase letter.")

    # Function to validate phone input is written in a specific format
    def validate_phone(self, phone):
        ph = re.compile(r'[0-9]{4}-[0-9]{3}-[0-9]{4}$')
        if not ph.match(self.phone.data):
            raise ValidationError("Phone must be in the following format: XXXX-XXX-XXXX")


class LoginForm(FlaskForm):  # Login form containing all the input fields
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField()'''

