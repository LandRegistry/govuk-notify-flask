from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Email

TITLES = [('', 'Please select a title'),
          ('Mr', 'Mr'),
          ('Mrs', 'Mrs'),
          ('Ms', 'Ms'),
          ('Miss', 'Miss')]


class PasswordReset(FlaskForm):
    email_address = StringField('Email Address', validators=[DataRequired(), Email()])
    title = SelectField('Title', choices=TITLES, validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    token = StringField('Token', validators=[DataRequired()])
