from smtplib import SMTP
import smtplib, os
from datetime import date 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# password = os.environ.get("EMAIL_PASSWORD_CODE")
# print(type(password))
body_txt = f"Hello, here are {date.today()} daily reports."
body = body_txt
message = MIMEMultipart()
message.attach(MIMEText(body,'plain'))

text = message.as_string()

try:
    server = SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("adapalapavan5@gmail.com", "#############")
    print("connected")
    server.sendmail("adapalapavan5@gmail.com", 'pavankumar.biw@gmail.com', text)
    server.quit()
except smtplib.SMTPException as e:
    print(e)
