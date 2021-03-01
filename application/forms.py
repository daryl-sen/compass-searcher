from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class login_form(FlaskForm):
  username = StringField(validators=[DataRequired("Your username is required for login.")])
  password = PasswordField(validators=[DataRequired("Your password is required for login")])
  submit = SubmitField("Log In")