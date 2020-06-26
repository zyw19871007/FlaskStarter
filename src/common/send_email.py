import smtplib
from email.mime.multipart import MIMEMultipart


def send_mail(to_email, subject, message, server='smtp.qq.com', port=465,
              from_email='email_address'):
    # import smtplib
    print("send email")
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ', '.join(to_email)

    msg.attach(message)
    print('email server')
    server = smtplib.SMTP_SSL(server, port)
    # server.set_debuglevel(1)
    server.login(from_email, 'token')  # user & password
    server.send_message(msg)
    server.quit()
    print('successfully sent the mail.')
