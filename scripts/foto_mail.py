import smtplib
from datetime import datetime
from email.message import EmailMessage
import imghdr


#Zamanı ayarlıyorum.Bunu kendime mail atacağım.
time = datetime.now()
time = str(time)
time = time[11:19]+', '+time[8:10]+'.'+time[5:7]+'.'+time[:4]

EMAIL_ADRESS = 'bothasanaslan@gmail.com'
EMAIL_PASSWORD = '8448209aAbot'
receiver = 'aslanhassan98@gmail.com'

msg= EmailMessage()
msg['Subject'] = 'Aslan bot uploader'
msg['From'] = EMAIL_ADRESS
msg['To'] = receiver
msg.set_content('This files have been sent by aslanbot.')

files = ['1.jpg','2.jpg']
for file in files:
    with open(file,'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data,maintype='image',subtype=file_type,filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)