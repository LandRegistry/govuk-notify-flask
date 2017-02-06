from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

TITLES = [('', 'Please select a title'),
          ('Mr', 'Mr'),
          ('Mrs', 'Mrs'),
          ('Ms', 'Ms'),
          ('Miss', 'Miss')]


class PasswordReset(FlaskForm):
    email_address = StringField('Email Address', validators=[DataRequired(), Email()])
    title = SelectField('Title', choices=TITLES, validators=[DataRequired()])
    forename = StringField('First Name', validators=[DataRequired()])
    surname = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('New Password', validators=[DataRequired(),
                             EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password', validators=[DataRequired()])
