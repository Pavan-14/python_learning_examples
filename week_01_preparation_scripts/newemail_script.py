import smtplib
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import date
import os
import schedule
import time
import email_log


running = True


def daily_report():
    sender_email = "adapalapavan5@gmail.com"
    receiver_email = ["pavankumar.biw@gmail.com","pavankumaradapala.deu@gmail.com"]
    password = os.environ.get('EMAIL_PASSWORD_CODE')
    body_txt = f"Hello, here are {date.today()} daily reports."

    # email details
    message = MIMEMultipart()
    message['From'] = sender_email
    if len(receiver_email) > 1:
        message['To'] = ",".join(receiver_email)
    else:
        message['To'] = receiver_email
    message['Subject'] = f"{date.today()} daily reports."
    body = body_txt
    message.attach(MIMEText(body,'plain'))


    # To get report files
    def reportfiles_list(path:str):
        files_list = []
        if os.path.exists(path):
            for file in os.listdir(path):
                files_list.append(os.path.join(path,file))
        else:
            print(f"{path} not exist")
        return files_list
    
    # calling the reportfiles function
    path = "C:\\Users\\Adapala\\Desktop\\Scholarship_app_Adapala\\"
    report_files = reportfiles_list(path)

    if len(report_files) != 0:
        for file in report_files:
            part = MIMEBase('application','octet-stream')
            # attaching files
            try:
                with open(file,'rb') as attachment:
                    part.set_payload((attachment).read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition',"attachment; filename= "+file)
                    message.attach(part)
            except FileNotFoundError as e:
                email_log.logger.error("Exception Occured",exc_info=True)
            except FileExistsError as err:
                email_log.logger.error("Exception Occured",exc_info=True)
    else:
        print(f"No files presented in {path}")

    text = message.as_string()


    # SMTP server instance
    try:
        server = SMTP('smtp.gmail.com', 587)
        server.starttls()
        if password == None:
            print("email password not available")
        else:          
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        server.quit()
    except smtplib.SMTPException as e:
        email_log.logger.error("Exception Occured",exc_info=True)




    global running
    running = False
    print("stopped")
    return schedule.CancelJob

schedule.every(5).minutes.do(daily_report)

# schedule.every().day.at("06:00").do(daily_report)


while running:
    schedule.run_pending()
    time.sleep(1)
