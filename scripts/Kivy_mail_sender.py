import os
import json
import smtplib
from email.message import EmailMessage
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.core.window import Window


Window.size = (400, 500)
#load data from my database
with open('mail.json','r') as f:
    my_info = json.load(f)

encrypted_mail = my_info['address']
encrypted_password = my_info['password']

EMAIL_ADRESS = ''
EMAIL_PASSWORD = ''


#dosyaları ekleyecek.
dizinler = []



codex = {
        "\n": "\n",
        "\t": "\t", "1": "q", "x": "b", "£": "p", "s": "u", "Ò": "{", "ñ": "Ÿ", "ï": "M", "K": "ç", ">": "È", "F": "!",
        ".": "Ç", "9": "ş", "4": "^", "Â": "Ó", "è": "~", "B": "ì", ",": "n", "e": "Z", "8": "5", "¾": "}", "P": "Ã",
        "d": "Î", "î": "m", "g": "#", "j": "õ", "+": "2", "ä": "r", "ã": "N",
        "ý": "û", "ı": "Ü", "ÿ": "3", "V": "U", "T": "ô", "a": "k", "o": "i",
        "Û": "Ô", "Ñ": "c", "W": "O", "Á": "ú", "ß": "Ý", "â": "Ì", "(": "D",
        "E": "R", "É": "]", "H": "Í", "G": "Y", ")": "ù", "I": "f", "'": "'",
        "X": "y", "<": "ê", "À": "w", "Ê": " ", "ö": "[", "Ú": "ğ", "½": "t",
        "Q": "ó", "_": "L", "&": "ü", "=": ";", "å": "0", "ò": "İ", "Ù": "á",
        "l": "Ğ", "7": "—", "%": "$", "ë": "Õ", "J": "A", "Ş": "?", "z": "/", "6": "h", "S": "à", "é": "C", "-": "í",
        ":": "Ö",
        "@": 'v',
        "q": "1", "b": "x", "p": "£", "u": "s", "{": "Ò", "Ÿ": "ñ", "M": "ï", "ç": "K", "È": ">", "!": "F",
        "Ç": ".", "ş": "9", "^": "4", "Ó": "Â", "~": "è", "ì": "B", "n": ",", "Z": "e", "5": "8", "}": "¾", "Ã": "P",
        "Î": "d", "m": "î", "#": "g", "õ": "j", "2": "+", "r": "ä", "N": "ã",
        "û": "ý", "Ü": "ı", "3": "ÿ", "U": "V", "ô": "T", "k": "a", "i": "o",
        "Ô": "Û", "c": "Ñ", "O": "W", "ú": "Á", "Ý": "ß", "Ì": "â", "D": "(",
        "R": "E", "]": "É", "Í": "H", "Y": "G", "ù": ")", "f": "I", "v": "@",
        "y": "X", "ê": "<", "w": "À", " ": "Ê", "[": "ö", "ğ": "Ú", "t": "½",
        "ó": "Q", "L": "_", "ü": "&", ";": "=", "0": "å", "İ": "ò", "á": "Ù",
        "Ğ": "l", "—": "7", "$": "%", "Õ": "ë", "A": "J", "?": "Ş", "/": "z", "h": "6", "à": "S", "C": "é", "í": "-",
        'v': '@', "Ö": ":"
    }
#for decrypting
key_list = list(codex.keys())
val_list = list(codex.values())
print(encrypted_mail)
#set mail adresses and the passwords.
for a in encrypted_mail:
    if a=='"' or a=="'":
        pass
    else:
        EMAIL_ADRESS += key_list[val_list.index(a)]
for b in encrypted_password:
    if b=='"' or b=="'":
        continue
    EMAIL_PASSWORD+= key_list[val_list.index(b)]
print("Gönderici mail:",EMAIL_ADRESS)

os.system(f"title decyrpted info {EMAIL_ADRESS}")

class MainPage(BoxLayout):
    def dizin_ekle(self):
        global dizinler
        #işlem yapılacak dizin
        directory = self.ids.directory.text

        try:
            os.chdir(directory)
            self.ids.info.text= f'[color=#00FF00]{os.getcwd()}[/color]'
        except Exception as ff:
            self.ids.info.text= '[color=#FF0000]Hatali dizin![/color]'

        try:
            #dizinleri tek tek al ve birleştir
            dizin = self.ids.dosyalar.text.split('+++')
            for a in dizin:
                dizinler.append(a)
        except Exception as wtf:
            self.ids.info.text= f'[color=#FF0000]{wtf}![/color]'
        
        self.ids.dosyalar.text = ''
        self.ids.dizin_info.text= '[color=#FF0000]Mevcut Dosyalar:[/color]'
        
        if dizinler[0]:
            self.ids.dizin_info1.text= f'[color=#00FF00]{dizinler[0]}[/color]'
        try:
            if dizinler[1]:
                self.ids.dizin_info2.text= f'[color=#00FF00]{dizinler[1]}[/color]'
            if dizinler[2]:
                self.ids.dizin_info3.text= f'[color=#00FF00]{dizinler[2]}[/color]'
            if dizinler[3]:
                self.ids.dizin_info4.text= f'[color=#00FF00]{dizinler[3]}[/color]'
            if dizinler[4]:
                self.ids.dizin_info5.text= f'[color=#00FF00]{dizinler[4]}[/color]'
        except:
            pass
       

    def mail_send(self):
        global EMAIL_ADRESS, EMAIL_PASSWORD
       
        msg= EmailMessage()
        if self.ids.konu.text =='':
            msg['Subject'] = 'Bot Hasan Aslan'
        else:
            msg['Subject'] = self.ids.konu.text

        msg['From'] = EMAIL_ADRESS
        msg['To'] =  self.ids.alici.text
        #set message
        message = self.ids.mesaj.text
        msg.set_content(f'{message}\n\n\n\tThis messages/files have been sent by aslanbot.')
        try:
            for file in dizinler:
                with open(file,'rb') as f:
                    file_data = f.read()
                    file_name = f.name
                msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename = file_name)
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
                smtp.send_message(msg)
            self.ids.info.text= '[color=#FF0000]Gonderildi![/color]'
        except Exception as hmm:
            self.ids.info.text= f'[color=#FF0000]{hmm}[/color]'
            print(hmm)
        


class AslanMailSender(App):
    def build(self):
        return MainPage() 


if __name__=='__main__':
    AslanMailSender().run()

