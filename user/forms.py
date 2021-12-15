import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = StringField(validators=[DataRequired()])
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    confirm_password = PasswordField(validators=[DataRequired()])
    firstname = StringField(validators=[DataRequired()])
    lastname = StringField(validators=[DataRequired()])
    submit = SubmitField()

# Function used to exclude certain characters from user inputs
# def character_check(form, field):
#     excluded_chars = "*?!'^+%&/()=}][{$#@<>"
#     for char in field.data:
#         if char in excluded_chars:
#             raise ValidationError(
#                 f"Character {char} is not allowed.")
#
#
# # Validators lists all the types of inputs required for the submit
#
#     # Function to validate password input contains certain characters
#     def validate_password(self, password):
#         pa = re.compile(r'(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@<>?/.,"£$%^&=*():;+{}|_-])')
#         if not pa.match(self.password.data):
#             raise ValidationError("Password must contain at least: 1 digit, 1 special character,"
#                                   " 1 lowercase and 1 uppercase letter.")
#
#     # Function to validate phone input is written in a specific format
#     def validate_phone(self, phone):
#         ph = re.compile(r'[0-9]{4}-[0-9]{3}-[0-9]{4}$')
#         if not ph.match(self.phone.data):
#             raise ValidationError("Phone must be in the following format: XXXX-XXX-XXXX")
#
#
# class LoginForm(FlaskForm):  # Login form containing all the input fields
#     email = StringField(validators=[DataRequired(), Email()])
#     password = PasswordField(validators=[DataRequired()])
#     submit = SubmitField()

