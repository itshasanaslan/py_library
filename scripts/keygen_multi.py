# aynı key çıktıysa eşleşsin.
import random
from colorama import Fore, Style,init
from time import sleep

init()
green = Style.BRIGHT + Fore.GREEN
blue = Style.BRIGHT + Fore.BLUE
red = Style.BRIGHT + Fore.RED
magenta = Style.BRIGHT + Fore.MAGENTA

colors = [green, blue, red, magenta]

key_array = []
keys = "MKXTI9BERLWC1D7ZGP032AOF8NHYU4S6VQ5J"
box1, box2, box3, box4, box5 = "", "", "", "", ""
arrr = []
for a in keys:
    key_array.append(a)
count = 0
while True:
    try:
        user_time = int(input("How many key do you want?: "))
        issleep = input("Do you want to make it slower?")
        if issleep=="y" or issleep=="yes":
            user_zaman = float(input("And how often?; 0.1 or 0.03 "))
            if user_time>1:
                print("it is too long.. ")
        break
    except:
        print(red + "Enter a number!")



while True:
    new_color = random.choice(colors)
    box1, box2, box3, box4, box5 = "", "", "", "", ""
    while len(box1) != 5:
        letter = random.choice(key_array)
        box1 += letter
    new_array = []
    while len(box2) != 5:
        letter = random.choice(key_array)
        box2 += letter
    while len(box3) != 5:
        letter = random.choice(key_array)
        box3 += letter

    while len(box4) != 5:
        letter = random.choice(key_array)
        box4 += letter
    while len(box5) != 5:
        letter = random.choice(key_array)
        box5 += letter

    new_array.extend([box1, box2, box3, box4, box5])
    print("\t\t\t",*new_array, sep=" " + new_color)
    if issleep == "y" or issleep == "yes":
        sleep(user_zaman)
    count += 1
    if count == user_time:
        break
