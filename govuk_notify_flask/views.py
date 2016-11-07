from govuk_notify_flask import app
from flask import render_template
from govuk_notify_flask.forms import EmailForm
from notifications_python_client.notifications import NotificationsAPIClient

notifications_client = NotificationsAPIClient(app.config['NOTIFY_API_KEY'])


@app.route('/', methods=["GET", "POST"])
def index():
    email_form = EmailForm()
    if email_form.validate_on_submit():
        notifications_client.send_email_notification(
            email_form.email_address.data,
            email_form.template.data
        )
        return render_template(
            'index.html',
            form=email_form
        )

    return render_template(
        'index.html',
        form=email_form
    )
