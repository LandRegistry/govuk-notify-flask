from govuk_notify_flask import app
from flask import render_template
from govuk_notify_flask.forms import EmailForm
from notifications_python_client.notifications import NotificationsAPIClient

notifications_client = NotificationsAPIClient(app.config['NOTIFY_API_KEY'])


@app.route('/', methods=["GET", "POST"])
def about():
    email_form = EmailForm()
    if email_form.validate_on_submit():
        return render_template(
            'index.html',
            form=email_form
        )

    return render_template(
        'index.html',
        form=email_form
    )
