
import smtplib
from email.message import EmailMessage
from pathlib import Path
import os

EMAIL_ADRESS = 'bothasanaslan@gmail.com'
EMAIL_PASSWORD = '8448209aAbot'



def receive_path():
    while True:
        current_path = input("Enter a path, press enter for current path.\nPath:  ")
        if current_path =='' or current_path ==None:
            current_path = os.getcwd()
            break
        else:
            try:
                os.chdir(current_path)
                os.system(f'title MailBot on {current_path}')
                
                break
            except Exception as f:
                print(f)

    os.system(f"title MailBot on {current_path}")

numbered_files=[]

receive_path()

my_path = Path()

dir_files = []

while True:
    it_is_a_temp =False  #checks if you just want to send an empty message.
    item_list = [] #add items to this list. So you can select them just with number.
    number = 1
    is_wrong = False
    os.system('cls')
    for file in my_path.glob('*'):
        file = str(file)
        print(f'\t\t{number}-) {file}')
        number+=1
        if file in dir_files:
            continue
        dir_files.append(file)
    choose_files = input('Choose files, split with double comma: ').split(',,')
    for a in choose_files:
        if a=="temp":
            os.system('cls')
            it_is_a_temp=True
            break
        if a.isdigit():
            if int(a)>number:
                print("No such number!")
            else:
                numbered_files.append(dir_files[number+1])
        elif a not in dir_files:
            input(f'{a} does not exist!')
            choose_files.remove(a)
            is_wrong = True
            break
    if is_wrong:
        continue
    break


select_a_mail = input("Lütfen hedef maili giriniz: ")
if select_a_mail=="me" or select_a_mail==None or select_a_mail =="":
    receiver = 'aslanhassan98@gmail.com'
    print("Sizin hesabınıza gönderiyorum.")
else:
    receiver = select_a_mail


new_message = input('Bir mesaj gir: ')
print('Gönderiliyor...')

msg= EmailMessage()
msg['Subject'] = 'Bot Hasan Aslan'
msg['From'] = EMAIL_ADRESS
msg['To'] = receiver
msg.set_content(f'{new_message}\n\n\n\tThis messages/files have been sent by aslanbot.')


if not it_is_a_temp:
    files = choose_files
    for a in numbered_files:
        files.append(a)


    for file in files:
        with open(file,'rb') as f:
            file_data = f.read()
            file_name = f.name
        msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)

input('\n\n\nDosyalar gönderildi.')