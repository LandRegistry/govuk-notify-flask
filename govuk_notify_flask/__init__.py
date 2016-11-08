# flake8: noqa
from flask import Flask
from flask_compress import Compress
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)

#App config
app.config.from_pyfile('config.py')

# Flask Compress
Compress(app)

# CSRF Protection
CsrfProtect(app)

import govuk_notify_flask.views
