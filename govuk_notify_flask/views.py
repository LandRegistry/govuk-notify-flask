from govuk_notify_flask import app
from flask import render_template, flash
from govuk_notify_flask.forms import EmailForm
from notifications_python_client.notifications import NotificationsAPIClient

notifications_client = NotificationsAPIClient(api_key=app.config['NOTIFY_API_KEY'])


@app.route('/', methods=["GET", "POST"])
def index():
    email_form = EmailForm()
    if email_form.validate_on_submit():
        notifications_client.send_email_notification(
            email_form.email_address.data,
            email_form.template.data
        )
        flash('Email sent')
        return render_template(
            'index.html',
            form=email_form
        )

    return render_template(
        'index.html',
        form=email_form
    )


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
