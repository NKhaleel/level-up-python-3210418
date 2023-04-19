import smtplib  # sending function
from email.mime.text import MIMEText

# port = 587 # SSL
sender_email = "xxxx@gmail.com"  # sender email (mine)
password = "xxxx"  # password here, could use user input()


def send_email(email, subject, message_body):

    message = MIMEText(message_body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = email

    with smtplib.SMTP_SSL("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, email, message.as_string())
