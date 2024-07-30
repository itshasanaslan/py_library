import smtplib
from email.mime.text import MIMEText
import random
import re


pattern = r"([\w\.-]+)@([\w\.]+)([\.\w]+)"
EMAIL_ADDRESS ='bothasanaslan@gmail.com'
PASSWORD = '8448209aAbot'
sub = 'Loyal Buddy Authentication'
user_mail = 'aslanhassan98@gmail.com'


def send_email(subject,msg,user_mail):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS,PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject,msg)
        server.sendmail(EMAIL_ADDRESS,user_mail,message)
        server.quit()
    except Exception as f:
        print(f)

def create_authentication_code():
	list_letters=[]
	letters= 'abcdefghijklmnoprstuvyzqwxABCDEFGHJIKLMNOPRSTUVYZWQX0123456789'
	for a in letters:
		list_letters.append(a)

	authentication_code = ''
	random.shuffle(list_letters)

	for element in range(8):
		temp_code = random.choice(list_letters)
		authentication_code += temp_code

	return authentication_code

authentication_code = create_authentication_code()
print(authentication_code)


def receive_user_mail_and_send(authentication_code):
	my_email = ''
	while True:
	        user_mail = input('\n\nEnter your mail address: ')
	        try:
	            global email
	            email = re.search(pattern, user_mail)
	            print(email.group())
	            email = email.group()
	            break
	        except:
	            print("Please enter a valid e-mail!")
	            continue
	print("E-mail accepted and sending your code..")

	ms = f"Your code to log in: {authentication_code} \nPlease do not share this code!"
	send_email(sub,ms,user_mail)



def take_code_and_check(authentication_code):
	attempts = 3
	while attempts>0:
		print(f"\n\n#######You have {attempts} attempts left.########")
		check_code = input("Enter your code:")
		attempts -=1
		if check_code!=authentication_code:
			print("Invalid code!")
		else:
			print('\n\nCode is accepted. Welcome!')
			break


receive_user_mail_and_send(authentication_code)
take_code_and_check(authentication_code)
input()
