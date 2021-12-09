from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

'''
from wtforms.validators import Required, Email


class LoginForm(FlaskForm):
    username = StringField(validators=[Required(), Email()])
    password = PasswordField(validators=[Required()])
    submit = SubmitField()
'''


class RegisterForm(FlaskForm):
    username = StringField()
    password = PasswordField()
    submit = SubmitField()
