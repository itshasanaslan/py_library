import os
from colorama import Fore, Style, init
import smtplib
import datetime
from email.mime.text import MIMEText
from time import sleep
from sys import stdout


os.system('@echo off')
os.system('title Aslan Bot')

time = datetime.datetime.now()
time = str(time)
EMAIL_ADDRESS = 'bothasanaslan@gmail.com'
PASSWORD = '8448209aAbot'
my_email = 'aslanhassan98@gmail.com'
ms = f'Your pc is opened at {time[:19]}'
sub = 'Aslan Security Bot'


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(EMAIL_ADDRESS, my_email, message)
        server.quit()
    except Exception as f:
        print(f)


send_email(sub, ms)

init()
red = Style.BRIGHT + Fore.RED
yellow = Style.BRIGHT + Fore.YELLOW
default = Style.RESET_ALL
green = Style.BRIGHT + Fore.GREEN

clear = lambda: os.system('cls')


def hide_protocol():
    os.system(
        'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced /v Hidden /t REG_DWORD /d 1 /f')
    os.system(
        'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced /v ShowSuperHidden /t REG_DWORD /d 1 /f')


os.system('powercfg setactive 381b4222-f694-41f0-9685-ff5bb260df2e')
os.system('attrib +h +s D:\\Hasan')
os.system('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced /v Hidden /t REG_DWORD /d 0 /f')
os.system('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced /v ShowSuperHidden /t REG_DWORD /d 0 /f')


try:
    with open('D:\\Hasan\\çalışma\\admin\\psw.txt', 'r') as f:
        my_real_pass = f.read()

except Exception as wtf:
    input(wtf)


def pass_manager():
    for cd in f"{red}All protocols are being applied. An e-mail has been sent to your mail to inform.\n":
        print(cd,end='')
        stdout.flush()
        sleep(0.03)
    while True:
        my_pass = input('Enter your password: ')
        if my_pass == my_real_pass:
            for c in f'{red}Welcome.. Please wait.':
                print(c,end='')
                stdout.flush()
                sleep(0.04)
            break
        else:
            exit()



def main_menu():
    clear()
    while True:
        print(f'''
            {red}[1]{yellow} to disable hiding operations.
            {red}[2]{yellow} to set power options.
            ''')
        main_menu_input = input('>>')
        if main_menu_input == '1':
            hide_protocol()
        print(f'{green}All files are visible.Type 2 to hide.{default}')
        in_main_menu = input('>>')
        if in_main_menu == '2':
            os.system(
                'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced /v Hidden /t REG_DWORD /d 0 /f')
            os.system(
                'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced /v ShowSuperHidden /t REG_DWORD /d 0 /f')
            print(f'{green}All files are invisible.{default}')
            input()
            clear()
        elif main_menu_input == '2':
            power_menu()
            clear()


def set_power_mode(power_code):
    os.system(f'powercfg setactive {power_code}')


def power_menu():
    clear()
    while True:
        print(f'''
            {red}[1]{yellow} Torrent/Download Mode
            {red}[2]{yellow} Balanced
            {red}[3]{yellow} Maximum Performance
            {red}[4]{yellow} Status{default}
            {red}[5]{yellow} to return
            {red}[q] to exit program.{default}
            ''')
        power_menu_input = input('>>')
        if power_menu_input == '1':
            set_power_mode('eca3a73c-f171-4803-b968-5cc2a62cb605')
            clear()
            print(f"{green}Torrent mode activated.{default}")
        elif power_menu_input == '2':
            set_power_mode('381b4222-f694-41f0-9685-ff5bb260df2e')
            clear()
            print(f"{green}Balanced mode activated.{default}")
        elif power_menu_input == '3':
            set_power_mode('e49262b1-3fc1-4962-adf3-7d2c549fc7df')
            clear()
            print(f"{green}Maximum performance mode activated.{default}")
        elif power_menu_input == '4':
            print(f"{green}Status:", end=' ')
            os.system('powercfg -list')
            input()
            clear()
        elif power_menu_input == '5':
            break
        elif power_menu_input == 'q':
            exit()
        else:
            print(f"{red}>>>Invalid Command!{default}")
            input()
            clear()


pass_manager()
main_menu()
