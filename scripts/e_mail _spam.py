import smtplib
import datetime
from email.mime.text import MIMEText

time = datetime.datetime.now()
time = str(time)
EMAIL_ADDRESS ='bothasanaslan@gmail.com'
PASSWORD = '8448209aAbot'
my_email = input('Enter the mail: ')
ms = input("Enter the msg: ")
sub = 'Aslan Security Bot'
def send_email(subject,msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS,PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject,msg)
        server.sendmail(EMAIL_ADDRESS,my_email,message)
        server.quit()
    except Exception as f:
        print(f)

aa = 1
while True:
	print(aa)
	send_email(sub,ms)
	aa+=1