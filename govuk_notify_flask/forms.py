from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Email

EMAILS = [('e389a7f6-fc65-4b32-9d85-ed067e726735', 'Hello World')]

TEXTS = [('e1d9690c-2f40-4de0-8417-087f389b3e3f', 'Hello World')]


class EmailForm(FlaskForm):
    email_address = StringField('Email Address', validators=[DataRequired(), Email()])
    template = SelectField('Template', choices=EMAILS, validators=[DataRequired()])


class TextForm(FlaskForm):
    mobile_number = StringField('Mobile Number', validators=[DataRequired()])
    template = SelectField('Template', choices=TEXTS, validators=[DataRequired()])
