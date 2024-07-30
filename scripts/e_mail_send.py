import smtplib
from email.mime.text import MIMEText

EMAIL_ADDRESS ='bothasanaslan@gmail.com'
PASSWORD = '8448209aAbot'
my_email = 'aslanhassan98@gmail.com'
ms = f''
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


send_email(sub,ms)