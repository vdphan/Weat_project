import django
django.setup()

import os
import smtplib, ssl
from apscheduler.schedulers.blocking import BlockingScheduler
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from weats.models import UserInfo


#django.setup()
load_dotenv()

sched = BlockingScheduler()
@sched.scheduled_job('interval', minutes=1)
#@sched.scheduled_job('cron', day_of_week='mon-sun', hour=8)
def send_email():
    data = UserInfo.objects.all()

    sf_list = []
    oak_list = []
    berkeley_list = []

    for user in data:
        if user.location.lower() == "berkeley":
            berkeley_list.append(user.email)
        elif user.location.lower() == "oakland":
            oak_list.append(user.email)
        elif user.location.lower() == "san francisco":
            sf_list.append(user.email)

    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "weat4747@gmail.com"
    password = os.getenv("PASS_EMAIL")
    if len(berkeley_list) != 0:
        receiver_email = ", ".join(berkeley_list)
        message = MIMEMultipart("alternative")
        message["Subject"] = "Hello from We@t"
        message["From"] = sender_email
        message["To"] = receiver_email
        text = """\
            Good morning!"""
        html = """\
            <html>
                <body>
                    <p>This is your linked to all recommended restaurant<br>
                    <a href="https://weat-app.herokuapp.com/search?q=Berkeley"><strong>Click here</strong></a>
                    </p>
                </body>
            </html>
            """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

    if len(oak_list) != 0:
        receiver_email = ", ".join(oak_list)
        message = MIMEMultipart("alternative")
        message["Subject"] = "Hello from We@t"
        message["From"] = sender_email
        message["To"] = receiver_email
        text = """\
            Good morning!"""
        html = """\
            <html>
                <body>
                    <p>This is your linked to all recommended restaurant<br>
                    <a href="https://weat-app.herokuapp.com/search?q=Oakland"><strong>Click here</strong></a>
                    </p>
                </body>
            </html>
            """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

    if len(sf_list) != 0:
        receiver_email = ", ".join(sf_list)
        message = MIMEMultipart("alternative")
        message["Subject"] = "Hello from We@t"
        message["From"] = sender_email
        message["To"] = receiver_email
        text = """\
            Good morning!"""
        html = """\
            <html>
                <body>
                    <p>This is your linked to all recommended restaurant<br>
                    <a href="https://weat-app.herokuapp.com/search?q=San+Francisco"><strong>Click here</strong></a>
                    </p>
                </body>
            </html>
            """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
sched.start()
