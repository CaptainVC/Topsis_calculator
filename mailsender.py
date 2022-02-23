import smtplib

from flask import flash
from credentials import email, password
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

fileName = "101917060-result.csv"

def send_mail(emailid):

    message = MIMEMultipart()
    attachment = open(fileName,"rb")
    p = MIMEBase('application','octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" %fileName)
    message.attach(p)
    attachment.close()


    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(email,password)
    text = message.as_string()
    server.sendmail(email,emailid,text)
    server.quit()
    os.remove(fileName)