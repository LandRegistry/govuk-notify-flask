import json
from govuk_notify_flask import app
from flask import render_template, flash
from govuk_notify_flask.forms import PasswordReset
from flask_wtf.csrf import CSRFError
from notifications_python_client.notifications import NotificationsAPIClient
from notifications_python_client.errors import HTTPError

notifications_client = NotificationsAPIClient(app.config['NOTIFY_API_KEY'])


@app.route('/', methods=["GET", "POST"])
def index():
    password_reset_form = PasswordReset()
    if password_reset_form.validate_on_submit():
        try:
            response = notifications_client.send_email_notification(
                email_address=password_reset_form.email_address.data,
                template_id='1e6a28c8-3555-4e10-897d-8d19ad058598',
                personalisation={
                    'title': password_reset_form.title.data,
                    'forename': password_reset_form.forename.data,
                    'surname': password_reset_form.surname.data,
                    'password': password_reset_form.password.data
                },
                reference=None
            )
            flash("Notification ID: " + response['id'])
        except HTTPError as e:
            raise e

        return render_template(
            'index.html',
            form=password_reset_form,
            response=json.dumps(response)
        )

    return render_template(
        'index.html',
        form=password_reset_form
    )


@app.errorhandler(CSRFError)
def handle_csrf_error(error):
    return render_template('error.html', error=error), 400


@app.errorhandler(400)
def bad_request(error):
    return render_template('error.html', error=error), 400


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error=error), 404


@app.errorhandler(429)
def exceeded_limit(error):
    return render_template('error.html', error=error), 429


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error=error), 500
