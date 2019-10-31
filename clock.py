import os
import smtplib, ssl
from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv


load_dotenv()
sched = BlockingScheduler()
@sched.scheduled_job('interval', minutes=1)
#@sched.scheduled_job('cron', day_of_week='mon-sun', hour=8)
def send_email():
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "weat4747@gmail.com"
    receiver_email = "vuphan1996@gmail.com"
    password = os.getenv("PASS_EMAIL")
    message = """\
        Subject: Hi there

        This message is sent from Python."""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
sched.start()
