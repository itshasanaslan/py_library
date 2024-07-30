#yeni sifre oluştur kısmından ana ekrana yönlendir. Mail gönderme commentli. Forgot password kısmından aktif et.
# Login screen ana ekrana yönlendirsin.Ana ekran tasarla.
# when converting to exe, try adding encoding ='utf8' inside the every with open()command. with open('file','r'encoding='utf8')
#forgot password kısmında email göndermeyi aktifleştir.
#mail log entrysini kaydetsin.
#ayarlar paneli ekle. Şifre, mail, kullanıcı adı değişsin. Zamanı maille haber versin. executer scripti ile koordineli çalışıp dosyaları silmeyi kaldırsın. Sadece gizleme özelliği de koy isteyene.
import os
import sys
import shutil
import getpass
import json
import re
import smtplib
from random import choice, shuffle
from email.mime.text import MIMEText
from time import sleep
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout #bunu sonra kontrol et.
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from time import sleep
from datetime import datetime,timedelta
from dateutil.parser import parse

#Window.borderless = True
Window.size = (400, 500)
clear = lambda:os.system('cls')
os.system('title Safe Death')

#these variables is for testing. When the app is finished, connect them properly.
db_user_password = ''
db_username = ''
db_user_email = ''
db_user_email_log = 0

authentication_code_for_mail = ''
#for forgot password section.
def create_authentication_code():
	list_letters=[]
	letters= 'abcdefghijklmnoprstuvyzqwxABCDEFGHJIKLMNOPRSTUVYZWQX0123456789'
	for a in letters:
		list_letters.append(a)

	authentication_code = ''
	shuffle(list_letters)

	for element in range(8):
		temp_code = choice(list_letters)
		authentication_code += temp_code

	return authentication_code
#to block user to trick program by pressing submit code without a code is generated.
authentication_code_for_mail = create_authentication_code()

#for mail authentication
program_EMAIL_ADDRESS ='bothasanaslan@gmail.com'
program_PASSWORD = '8448209aAbot'
mail_sub = 'Loyal Buddy Authentication'



def send_email(subject,msg,user_mail):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(program_EMAIL_ADDRESS,program_PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject,msg)
        server.sendmail(program_EMAIL_ADDRESS,user_mail,message)
        server.quit()
    except Exception as f:
        print('\n\n######',f)



first_dir = os.getcwd() #this will be necessary later.
#username = getpass.getuser() #this will be useful for file directories.

username = 'cadge'
check_pass = '' #declare this variable as a string
log_entries = 0


#my_loyal_buddy script required to be executed automatically when the pc is started.
#So, i need to move it to the startup folder.
auto_file_target= os.path.join('C:', os.sep, 'Users', username, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu',
                             'Programs','Startup')
auto_file_source = 'my_loyal_buddy.py'
auto_file_on_target =os.path.join('C:', os.sep, 'Users', username, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu',
                             'Programs','Startup','my_loyal_buddy.py')


#at first running, it checks whether it is installed before. If not, it will move the 'delete' executer to the startup.
is_executer_exist = False
password_exist = False

try:
    with open('my_loyal_buddy.py','r') as f:
        f.read()
        print('\n\n######Setting executer... ')
        shutil.copy(auto_file_source,auto_file_target)
        input('You can now delete my_loyal_buddy.py file.(Don\'t run it.)\nPress any key to continue.')
        is_executer_exist = True
except FileNotFoundError:
    try:
        with open(auto_file_on_target,'r') as f:
            f.read()
            print('\n\n######Executer is ready.')
            is_executer_exist = True
    except Exception as wtf:
        print('\n\n######This program requires my_loyal_buddy_py script for first time running.')
        print(f'Put the script in the same directory with this program.\nIf you have the script, rename it correctly.\nTo get the script, mail to me: aslanhassan98@gmail.com.')
        input(wtf)
    
except Exception as anotherException:
    input(anotherException)

#this will save your password in an encrypted way.
codex = {
        "\n": "\n",
        "\t": "\t", "1": "q", "x": "b", "£": "p", "s": "u", "Ò": "{", "ñ": "Ÿ", "ï": "M", "K": "ç", ">": "È", "F": "!",
        ".": "Ç", "9": "ş", "4": "^", "Â": "Ó", "è": "~", "B": "ì", ",": "n", "e": "Z", "8": "5", "¾": "}", "P": "Ã",
        "d": "Î", "î": "m", "g": "#", "j": "õ", "+": "2", "ä": "r", "ã": "N",
        "ý": "û", "ı": "Ü", "ÿ": "3", "V": "U", "T": "ô", "a": "k", "o": "i",
        "Û": "Ô", "Ñ": "c", "W": "O", "Á": "ú", "ß": "Ý", "â": "Ì", "(": "D",
        "E": "R", "É": "]", "H": "Í", "G": "Y", ")": "ù", "I": "f", "'": "v",
        "X": "y", "<": "ê", "À": "w", "Ê": " ", "ö": "[", "Ú": "ğ", "½": "t",
        "Q": "ó", "_": "L", "&": "ü", "=": ";", "å": "0", "ò": "İ", "Ù": "á",
        "l": "Ğ", "7": "—", "%": "$", "ë": "Õ", "J": "A", "Ş": "?", "z": "/", "6": "h", "S": "à", "é": "C", "-": "í",
        ":": "Ö",
        "@": '"',
        "q": "1", "b": "x", "p": "£", "u": "s", "{": "Ò", "Ÿ": "ñ", "M": "ï", "ç": "K", "È": ">", "!": "F",
        "Ç": ".", "ş": "9", "^": "4", "Ó": "Â", "~": "è", "ì": "B", "n": ",", "Z": "e", "5": "8", "}": "¾", "Ã": "P",
        "Î": "d", "m": "î", "#": "g", "õ": "j", "2": "+", "r": "ä", "N": "ã",
        "û": "ý", "Ü": "ı", "3": "ÿ", "U": "V", "ô": "T", "k": "a", "i": "o",
        "Ô": "Û", "c": "Ñ", "O": "W", "ú": "Á", "Ý": "ß", "Ì": "â", "D": "(",
        "R": "E", "]": "É", "Í": "H", "Y": "G", "ù": ")", "f": "I", "v": "'",
        "y": "X", "ê": "<", "w": "À", " ": "Ê", "[": "ö", "ğ": "Ú", "t": "½",
        "ó": "Q", "L": "_", "ü": "&", ";": "=", "0": "å", "İ": "ò", "á": "Ù",
        "Ğ": "l", "—": "7", "$": "%", "Õ": "ë", "A": "J", "?": "Ş", "/": "z", "h": "6", "à": "S", "C": "é", "í": "-",
        '"': '@', "Ö": ":"
    }
#create key variables for my codex .
key_list = list(codex.keys())
val_list = list(codex.values())


#check for user's password
def password_call():
  global password_exist, check_pass,db_username,db_user_password,db_user_email,db_user_email_log
  print('\n\n######Looking for database')
  log_entries = 0
  while True:
      
        output = ''
        if not os.path.exists('C:\ProgramData\Windows\critics\dic_data.json'):
            return False
            break
        if os.path.exists('C:\ProgramData\Windows\critics\dic_data.json'):
            with open('C:\ProgramData\Windows\critics\dic_data.json') as t:
                print('\n\nPath exists')
                user_data_dic = json.load(t)
                '''readpass = t.read()
                for b in readpass:
                    check_pass+=key_list[val_list.index(b)]'''
                db_username = user_data_dic['username']
                db_user_password = user_data_dic['password']
                db_user_email = user_data_dic['email']
                db_user_email_log = user_data_dic['email_sent']   
            return True #store the saved password.
        if log_entries==3:
            print('\n\n######Too many failed attempts!') 
            quit()
        elif not os.path.exists('C:\ProgramData\Windows\critics\dic_data.json'):
            return False



#first time exception pop-up
def LoyalFileNotFound():
    pop = Popup(title='Executer script not found!',
                  content=Label(text='This script requires my_loyal_buddy file for first time\n running.Please put it in the same directory.\nOtherwise, the program won\'t work\n\n\nMail: aslanhassan98@gmail.com'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()
    sleep(4)



class LogInScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.username_field.text = db_username #autofills the username section.
    '''
    def switchpages(self):
        print('\n\n######switching to sign in page.')
        run_this.screen_manager.current = 'Sign' '''

    def validate_user(self):
        global log_entries
        #run_this.screen_manager.current = 'Buraya istedigin ekranı gir.' # bu kodu kaldır
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        login_username = user.text
        login_pasw = pwd.text

        if login_username== '' or login_pasw=='':
            info.text = '[color=#FF0000]username and password required[/color]'
            
        else:
            if login_username==db_username and login_pasw ==db_user_password:
                info.text = '[color=#00FF00]WELCOME SIR[/color]'
            else:
                info.text = '[color=#FF0000]Invalid info![/color]'
                pwd.text = ''
                log_entries += 1
                print(f"log_entries:{log_entries}db_username = {db_username} pass {db_user_password}")
            if log_entries==3:
                os.system('rundll32.exe user32.dll, LockWorkStation')# Locks the PC after 3 failed login attempt.

    def go_to_pw_reset(self):
        print('\n\n######switching to reset pw')
        run_this.screen_manager.current = 'ForgotPassword'

#Forgot password screen
class ForgotPassword(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def proceed_to_login_page(self):
        run_this.screen_manager.current = 'LoginPage'

    def send_email(self):
        global db_user_email_log,authentication_code_for_mail
        info = self.ids.info
        if db_user_email_log>2:
            info.text = f'[color=#FF0000]We can send only two mails in a day![/color]'
        else:
            try:
                authentication_code_for_mail = create_authentication_code()
                send_this_mail_as_message = f'Authentication code to reset your password is: {authentication_code_for_mail} \nDo not share this code! '
                print(f"Authentication code is {authentication_code_for_mail}")
                #send_email(mail_sub,send_this_mail_as_message,db_user_email)
                db_user_email_log += 1
                info.text = f'[color=#00FF00]Mail is sent to {db_user_email}![/color]'
            except Exception as wtf:
                info.text = f'[color=#FF0000]{wtf}[/color]'
    def check_authentication_code(self):
        global authentication_code_for_mail
        info = self.ids.info
        code_entered = self.ids.code_field.text
        if code_entered ==authentication_code_for_mail:
            print('\n\n\n###Entered code:',code_entered,'while real code is:',authentication_code_for_mail)
            info.text = '[color=#00FF00]Code is correct![/color]'
            print('\n\n######Switching to ')
            sleep(4)
            run_this.screen_manager.current = 'CreateNewPassword'
        else:
            info.text = f'[color=#FF0000]Code is wrong![/color]'
            self.ids.code_field.text = ''

class CreateNewPassword(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    def check_passwords_and_save(self):
        global db_user_password
        #get the inputs
        first_password = self.ids.first_password_field.text
        second_password = self.ids.second_password_field.text
        info = self.ids.info

        if ' ' in first_password:
            info.text = '[color=#FF0000]Password cannot contain any space![/color]'
        elif len(first_password)<4:
            info.text = '[color=#FF0000]You need to use at least 4 characters![/color]'
        elif first_password!=second_password:
            info.text = '[color=#FF0000]Passwords does not match![/color]'
        else:
            info.text = '[color=#00FF00]saved![/color]'
            #save the passwords and redirect to apps main page.
            db_user_password = first_password
            print('\n\npassword is saved.')
            self.ids.first_password_field.text = ''
            self.ids.second_password_field.text = ''

class SignUpScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def validate_user(self):
        global db_username,db_user_password,db_user_email,db_user_email_log,password_exist
        #get variables from text inputs.
        user = self.ids.username_field
        pwd = self.ids.pwd_field

        check_pwd = self.ids.pwd_field_check
        user_email = self.ids.e_mail_field
        
        info = self.ids.info # error label.

        #create a mail pattern to check if the mail address is valid.
        mail_pattern = r"([\w\.-]+)@([\w\.]+)([\.\w]+)"
        is_mail_valid = False
        
        #check_mail = re.search(mail_pattern, email)
        try:
            check_this_email = re.search(mail_pattern,user_email.text)
            check_this_email = check_this_email.group()
            print(check_this_email)
            print('\n\n######mail is valid')
            is_mail_valid = True
        except Exception as wtff:
            print(wtff)
            print('\n\n######Mail is not valid!')
            is_mail_valid = False
         

        login_username = user.text
        login_pasw = pwd.text

        if login_username== '' or login_pasw=='' or user_email.text =='' or check_pwd.text=='':
            info.text = '[color=#FF0000]You need to fill all forms![/color]'
        elif pwd.text!=check_pwd.text:
            info.text = '[color=#FF0000]Passwords does not match![/color]'
        elif len(login_pasw)<4:
            info.text = '[color=#FF0000]Password should be at least 4 characters length![/color]'
        elif not is_mail_valid:
            info.text = '[color=#FF0000]Mail pattern should be "mymailaddress@mail.com"![/color]'
        else:
            info.text = '[color=#00FF00]Account Created! Redirecting to Log in page.[/color]'
            #save user data.
            user_data_store = {'username':login_username, 'password':login_pasw,'email':user_email.text,'email_sent':0}
            #initialized these in case they will be useful for account info changing.
            db_username = login_username
            db_user_password = login_pasw 
            db_user_email = user_email.text
            db_user_email_log = 0
            with open('C:\ProgramData\Windows\critics\dic_data.json','w') as save_this_info:
                json.dump(user_data_store,save_this_info)
                print('\n\n###Data saved!')
            password_exist = True
            run_this.screen_manager.current = 'LoginPage'

class MyApp(App):
    db_username_in_class = db_username
    def build(self):
        self.screen_manager =  ScreenManager()

        #initialize login page.
        self.login_page = LogInScreen()
        screen_login = Screen(name='LoginPage')
        screen_login.add_widget(self.login_page)

        #initialize forgot password page.
        self.forgot_password = ForgotPassword()
        screen_forgot_password = Screen(name='ForgotPassword')
        screen_forgot_password.add_widget(self.forgot_password)

        #initialize creating new password page.
        self.create_new_password = CreateNewPassword()
        screen_create_new_password = Screen(name='CreateNewPassword')
        screen_create_new_password.add_widget(self.create_new_password)

        #initialize sign up page.
        self.create_account_page = SignUpScreen()
        screen_create_account_page = Screen(name='Sign')
        screen_create_account_page.add_widget(self.create_account_page)
        
        if not is_executer_exist:
            return LoyalFileNotFound()
        
        if not password_exist:
            print('\n\n\n##New user detected.Creating new one.')
            #if new user, start from the create account page.
            self.screen_manager.add_widget(screen_create_account_page)

        #add your initialized widgets here. Eklediğim ekranları başlat.
        self.screen_manager.add_widget(screen_login)
        self.screen_manager.add_widget(screen_forgot_password)
        self.screen_manager.add_widget(screen_create_new_password)
        #self.screen_manager.add_widget(screen_create_account_page) #deneysel. Bunu sonra sil. Login butonundaki fonksiyondan da sil.
        return self.screen_manager

#check for passwords. If it is empty, it means it is first setup.
password_exist = password_call()

if __name__=='__main__':
    run_this = MyApp()
    run_this.run()


#en son verileri kaydet.
user_last_data = {
    'username':db_username,
    'password':db_user_password,
    'email' : db_user_email,
    'email_sent':db_user_email_log
}

print('\n\nTerminating..')
for item,key in user_last_data.items():
    print(item,':',key)

with open('C:\ProgramData\Windows\critics\dic_data.json','w') as tt:
    json.dump(user_last_data,tt)
