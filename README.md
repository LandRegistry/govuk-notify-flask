# GOV.UK Notify Flask Example
[![Build Status](https://travis-ci.org/LandRegistry/govuk-notify-flask.svg?branch=master)](https://travis-ci.org/LandRegistry/govuk-notify-flask)
[![Requirements Status](https://requires.io/github/LandRegistry/govuk-notify-flask/requirements.svg?branch=master)](https://requires.io/github/LandRegistry/govuk-notify-flask/requirements/?branch=master)

Example using GOV.UK Notify service through a Flask app

## Getting Started

```
git clone git@github.com:LandRegistry/govuk-notify-flask.git
cd govuk-notify-flask
pip3 install -r requirements.txt
export SECRET_KEY=<your_secret_key>
export NOTIFY_API_KEY=<your_api_key>
export FLASK_APP=govuk_notify_flask/__init__.py
export FLASK_DEBUG=1
```

## Testing
```
pip3 install -r requirements_test.txt
flake8 .
```

## Running

```
python3 -m flask run
```
