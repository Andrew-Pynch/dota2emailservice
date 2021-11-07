import codecs
import smtplib
import sys

# setting path
sys.path.append("../")

import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# importing
from user.user import User
from util.util import *


class EmailConfig(object):
    def __init__(self, password):
        self.port = 465  # For SSL
        self.smtp_server = "smtp.gmail.com"
        self.sender_email = "dota2statsservice@gmail.com"  # Enter your address
        self.test_receiver_email = (
            "andrewpynchbusiness@gmail.com"  # Enter receiver address
        )
        self.password = password  # Password for your gmail address
        # self.email_template = email_service.load_email_template_as_string()

    def __call__(self):
        pass

    def __str__(self):
        return f"""
    Port: {self.port}
    SMTP Server: {self.smtp_server}
    Sender Email: {self.sender_email}
    Test Receiver Email: {self.test_receiver_email}
    Password: *********************
        """


def get_email_template_as_string():
    file = codecs.open("template.html", "r")
    return file.read()


def get_email_template_with_data(user: User, email_template):
    new_email_template = email_template.replace("{first_name}", user.first_name)
    # new_email_template = new_email_template.replace("{first_name}", user.first_name)
    return new_email_template


def get_subject_dates():
    today = datetime.date.today()
    last_week = today - datetime.timedelta(days=7)
    return f"{last_week} - {today}"


def get_email_message(user: User, email_config: EmailConfig):
    html_template = get_email_template_with_data(user, get_email_template_as_string())

    message = MIMEMultipart("alternative")
    message["Subject"] = f"Dota2 Stats Summary {get_subject_dates()}"
    message["From"] = email_config.sender_email
    message["To"] = user.email

    # Turn these into plain/html MIMEText objects
    template_with_data = MIMEText(html_template, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(template_with_data)

    return message


def send_user_stats_email(
    user: User, server: smtplib.SMTP_SSL, email_config: EmailConfig
):
    print(f"Sending stats email to {user.first_name} {user.last_name} | {user.email}")
    message = get_email_message(user, email_config)
    server.sendmail(email_config.sender_email, user.email, message.as_string())
