# flake8: noqa
from flask import Flask
from flask_compress import Compress

app = Flask(__name__)

#App config
app.config.from_pyfile('config.py')

# Flask Compress
Compress(app)

import govuk_notify_flask.views
