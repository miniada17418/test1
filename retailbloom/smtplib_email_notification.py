import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def send_update_email(email_from, email_to, subject_line, file_attachment, message):
    email_user = email_from
    email_send = email_to
    subject = subject_line

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject
    body = message

    msg.attach(MIMEText(body,'plain'))

    try:
        if file_attachment:
            attach_file = file_attachment
            file_name = attach_file.split('/')
            print(file_name)
            attachment = open(attach_file, 'rb')

            part = MIMEBase('application',"octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition','attachment; filename="{}"'.format(file_name[-1]))

            msg.attach(part)
    except Exception as e:
        print(e)
        print('error while processing attachment')
    text = msg.as_string()

    mail = smtplib.SMTP("smtp.us.exg7.exghost.com",587)

    mail.ehlo()

    mail.starttls()

    mail.login(os.environ["email_user"], os.environ["email_pass"])

    mail.sendmail(os.environ["email_user"], os.environ["email_user"],text,)

    mail.quit()
