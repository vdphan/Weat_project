import smtplib, ssl


def send_email():
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "weat4747@gmail.com"
    receiver_email = "vuphan1996@gmail.com"
    password = "weat2122"
    message = """\
        Subject: Hi there

        This message is sent from Python."""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
