from os import system
import smtplib
import datetime
from email.mime.text import MIMEText

EMAIL_ADDRESS ='bothasanaslan@gmail.com'
PASSWORD = '8448209aAbot'
my_email = 'aslanhassan98@gmail.com'
decorator = '##################################################################################################'
kimlik = "\tSeri No: A12I64484\n\n"
banka_kart = "\t  ZIRAAT KART NO\n\t4766 1907 3400 8027\n\t\t01/28\n\t\t554\n\n"
kyk_kart = "\t  KYK KART NO\n\t5282 0802 5259 8636\n\t\t08/23\n\t\t061\n\n"
kyk_kredi = "\t  KREDI KART NO\n\t5235 2905 4935 5728\n\t\t08/23\n\t\t336"

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




while True:
	my_pass= input('Enter your pass: ')
	if my_pass!='8448209aA':
		time = datetime.datetime.now()
		time = str(time)
		ms = f'Birisi kimlik uygulamana erismeye calisti.Tarih: {time[:19]}'
		sub = 'Aslan ID Security Bot'
		send_email(sub,ms)
		exit()
	else:
		break
system('cls')
print(decorator)
print(kimlik)
print(decorator)
print(banka_kart)
print(decorator)
print(kyk_kart)
print(decorator)
print(kyk_kredi)
input()

