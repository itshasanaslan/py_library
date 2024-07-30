#en son, comment yaptıgın kod dizisini düzelt.Color manageer
# tüm hikayeyi yaz. Her canavaar ölürken konuşsun.
# canavar rastgele hp bassın güçlensin ya da zayıflasın.
# hangman guess game gibi puzlelar koy.

import random as r
import time
import os
import platform
from Monster import Monster
from colorama import Style, Fore, init
from Player import *
from wear_item import wear_item
from remove_item import remove_item
from color_manager import windows_color_manager
from codex import secret_codex
from items import *

init()
green = Style.BRIGHT + Fore.GREEN
blue = Style.BRIGHT + Fore.BLUE
red = Style.BRIGHT + Fore.RED
magenta = Style.BRIGHT + Fore.MAGENTA
yellow = Style.BRIGHT + Fore.YELLOW
default = Style.RESET_ALL
new_started = True
user_race = ''

clear = lambda:os.system('cls')
operation_system = ""
if platform.system() == 'Linux':
    operation_system = 'linux'
    clear = lambda: os.system('clear')
elif platform.system() == 'windows' or platform.system() == 'Windows' or 'windows' in platform.system():
    operation_system = 'windows'
    clear = lambda: os.system(('cls'))
    clear()
    #windows_color_manager()


clear()

player_skills_select_list, player_skills_values, player_skills_mana_cost = None, None, None
puzzle_box = []
codex_alphabet = []  # every item on secret message will be added to this list.
user_discovered_codex_alphabet = []  # Letters discovered by player will be added here.
used_user_discovered_codex_alphabet = []
codex_alphabet_equal = []  # this list will contain alphabets and their value; A=c
secret_message = "O6iZ'ZäÊIo#6½uÊîi,u½ZäuÊu6isĞÎÊuZZÊ½iÊo½Ê½6k½Êo,Ê½6ZÊ£äiÑZuuÊ6ZÊÎiZuÊ,i½ÊxZÑiîZÊkÊîi,u½ZäÇÊJ,ÎÊoIÊXisÊ#k/ZÊĞi,#ÊZ,is#6Êo,½iÊk,ÊkxXuunÊ½6ZÊkxXuuÊÀoĞĞÊ#k/ZÊxkÑaÊo,½iÊXisÇÊf,Ê½6ZÊZ,ÎnXisÊäZkĞo/ZnÊ½6ZÊäZkĞÊîi,u½ZäÊounÊWVEàR_URàÇÇÇÊÊÊÊIäiîÊÒZ,ÑäX£½ZÎL,kîZ¾"

monstersentences = ['I will not obey you!', 'You, a human-flesh! You think you can kill me?',
                    'You may be successful at killing me, but at what cost? He will find you!', 'I will kill you!',
                    "Noo, it can't be", 'In the end, you will meet him!', "I will drink your blood!",
                    "Ah, I was young just as you. You deserve this. I failed."]
generic_monster_sentences = ["You may hurt me. But killing me? That's impossible.", "I will sacrifice you to him!",
                             "You created me and now killing me. Why?", "You will never find out the mystery!",
                             "You are so easy.", "I will give you a secret. After I kill you!",
                             'We all are lost in this world. Don\'t you understand?', ]
used_monstersentences = []

for letter in secret_message:
    if letter not in codex_alphabet:
        codex_alphabet.append(letter)
    else:
        continue
r.shuffle(codex_alphabet)

decorators = "----------------------------------------------------------------------"
dwarf_sell_counter = 5


whole_item_control = []

for a in warrior_item:
    if a not in whole_item_control:
        whole_item_control.append(a)
for b in dwarf_item:
    if b not in whole_item_control:
        whole_item_control.append(b)
for c in elf_item:
    if c not in whole_item_control:
        whole_item_control.append(c)







def welcome_user():
    global new_started
    new_started = False
    input('At the dawn of a misty night, you are dreaming again.')
    input('The world you dream is beyond your perceptions.')
    input('You see the whole world in a rush.They are always after things urgently. Just like ants.')
    input('Then you see how the things are evolved in their hands.')
    input('You see people are living in peace and how easy their lives.')
    input('Families, friendships and other relationships. They are so innocent.')
    input('And you see someone who is doing something in the front of a device.')
    input(f"{green}You:{yellow} What is that thing?")
    input(f"{green}You: {yellow}Why he just sits and look at that box for hours and hours.")
    input(f'{default}Then, you see a massive light beam momentary.')
    input('Again.')
    input('Again..')
    input('And again..')
    input(f'{green}...{default}')
    clear()
    input('\nWaking up from the dream, you question your life again.')
    input(f'{green}You:{yellow} Why I always see this illusion.?{default}')
    input('You try to analyse  things but you never understand.')
    input('7 days ago, you woke up under a willow tree; not remembering anything. ')
    input('Not even a day, moment, even your name.')
    input(
        'The only thing you remember since you woke up under the tree that you are trying to find what happened to you.')
    input('Actually, you were looking for something which makes you drive insane;')
    input(f'{yellow}Who am I?')
    input(f'What\'s my name?{default}')

    while True:
        global username, user_race, player_wearable, player1, asell_multiply
        username = input(f"{magenta}\tEnter your name: {default}").title()
        if not any(c in "ABCDEFGĞHIİJKLMNOÖPRSŞTUÜWYZXQ1234567890abcçdefgğhıijklmnoöprsştuüvyzqwx" for c in username):
            print(red,"\tPlease use valid characters!",default)
            input(f'{magenta}\nPress anything to continue.{default}')
            clear()
            print('\nWaking up from the dream, you question your life again.')
            print(f'{green}You: {yellow}Why I always see this illusion.?{default}')
            print('You try to analyse  things but you never understand.')
            print('7 days ago, you woke up under a willow tree; not remembering anything. ')
            print('Not even a day, moment, even your name.')
            print(
                'The only thing you remember since you woke up under the tree that you are trying to find what happened to you.')
            print('Actually, you were looking for something which makes you drive insane;')
            print(f'{yellow}Who am I?')
            print(f'What\'s my name?{default}')
            continue
        clear()
        print(
            f"{green}\tWhich race do you want;{default}\n\tType '{red}1{default}' to choose '{red}Elf{default}'.\n\tType '{red}2{default}' to choose '{red}Warrior{default}'.\n\tType '{red}3{default}' to choose '{red}Dwarf{default}'.")
        user_race = input(f"\n{magenta}Enter your race please:{default} ")
        if user_race.lower() not in ["1", "2", "3", "elf", "dwarf", "warrior"]:
            clear()
            print(red,"\t\tInvalid option!",default)
            continue
        elif user_race == "1" or user_race.lower() == "elf":
            user_race = "Elf"
            player_wearable = elf_item
            item_tags.update({'ring': 8})
            item_tags.update({'bow': 8})
            item_tags.update({'shield': 6})
            asell_multiply = 0.80
        elif user_race == "2" or user_race.lower() == "warrior":
            user_race = "Warrior"
            player_wearable = warrior_item
            item_tags.update({'single sword': 7})
            item_tags.update({'great shield': 10})
            asell_multiply = 0.80
        elif user_race == "3" or user_race.lower() == "dwarf":
            user_race = "Dwarf"
            player_wearable = dwarf_item
            item_tags.update({'mighty ring': 18})
            asell_multiply = 1.3
        clear()
        player1 = Player(username)
        player1.player_race_optimize()
        input(f'{magenta}\n\nPress anything to continue..{default}')
        clear()
        return play_game()


def before_battle_prepare():
    player1.in_battle_mana = player1.mana_point
    player1.in_battle_heal_point = player1.heal_point


def game_over():
    print(decorators)
    print(decorators)
    print(decorators)
    print("\t YOU DID YOUR BEST, BUT THE MONSTER KILLED YOU.\n\tGAME OVER!")
    print(decorators)
    print(decorators)
    print(decorators)
    print("\n\n\t\tYou will start from the last checkpoint.Type play from the menu.")
    input("\n..........Press enter...... .")
    matrix(100)
    return take_action()


def in_battle():  # Prepares player info and arranges battle.
    global monster1, player1
    monster1 = Monster()
    monster1.monster_create()
    before_battle_prepare()
    while player1.in_battle_heal_point >= 0 or monster1.healpoint >= 0:
        if player1.in_battle_heal_point <= 0:
            game_over()
            break
        player1.player_attack()
        if monster1.healpoint <= 0:
            print(f"{red}\tSystem: {monster1.name} is dead{default}")
            monster1.drop_item()
            monster1.monster_dead = True
            player1.level_up()
            break
        monster1.attack()
    else:
        print("\tSystem: Battle is end.")
    print(f"{red}\tSystem:{green} The battle is end.{default}")
    input(f'{magenta}Press anything to continue.{default}')
    clear()


def matrix(num):
    symbols = ["0", "1", "   ", "uÊ,i½Êx", "u½Zä", " ", " ", "Êîi,u½ZäuÊu"]
    line = []
    counter = 0
    r_symbols = []
    for i in range(118):
        x = r.randint(0, 3)
        line.append(symbols[x])
        counter += 1

    for i in range(num):
        if counter % 5 == 0:
            r_symbols = [r.randint(0, 117) for x in range(10)]
        for i in r_symbols:
            line[i] = symbols[r.randint(0, 3)]
        colors = [red,blue,magenta,green,yellow]
        randomcolor = r.choice(colors)
        print(randomcolor,*line,default)
        counter += 1
        time.sleep(0.01)


chapter_one_complete = False


def play_game():
    def chapter_one():
        input(
            "When you look at your left, you see a river. Then you remember it.\nYou are moving to the river and washing your face.")
        input(
            "It gives you a bit relief. But don't satisfies at all. Suddenly, you become uncomfortable.\nYou start to remember things. You are a hunter.")
        input(
            "A hunter hunts the monsters. That's why you dressed different. After some time,\nyou take your bag and walk into the forest.")
        input("....")
        input(f'{green}Something happening to you.{default}')
        input('...')
        input('....')
        print("")
        matrix(210)
        clear()
        input(f"\n\n{green}{player1.name}:{yellow} What happened? My head.. .Ouch!{default}")
        input(f'{red}+{yellow}"He is here!"')
        input(f'{green}{player1.name}: {yellow}"What was that sound?"{default}')
        input(f'{red}+{yellow}"Ahh, finally, you are here."{default}')
        input(f'{green}You see a talking monster, which is similar to others you killed before.{default}')
        input(f'{green}{player1.name}: {yellow}"Who are you?"{default}')
        input(f"{red}+: {yellow}\"I've been waiting for you. So long...But, but the things have been changed. I will not deliver it before you kill me.\"{default}")
        input(f'{green}{player1.name}: {yellow}\"So it be!\"{default}')
        input(f"\t{blue}You draw your weapons quickly.{default}")
        # chapter 2'ye geç. Yaratık bilgisini düzgün göstert.
        in_battle()
        input(f"{default}After killing {monster1.name}, you see a paper in the ground.")
        while True:
            global chapter_one_complete
            chaponeinput = input(f"Press '{red}i{default}' to inspect it.").lower()
            if chaponeinput == 'i':
                clear()
                print('''\n\n\n
                        --------------------------------------------------
                       @O6iZ'ZäÊIo#6½uÊîi,u½ZäuÊu6isĞÎÊuZZÊ½iÊo½Ê½6k½Êo,
                       Ê½6ZÊ£äiÑZuuÊ6ZÊÎiZuÊ,i½ÊxZÑiîZÊkÊîi,u½ZäÇÊJ,ÎÊoI
                       ÊXisÊ#kZÊĞi,#ÊZ,is#6Êo,½iÊk,ÊkxXuunÊ½6ZÊkxXuuÊÀoĞĞÊ#
                       kZÊxkÑaÊo,½iÊXisÇ@Êf,Ê½6ZÊZ,ÎnXisÊäZkĞo/ZnÊ½6Z
                       ÊäZkĞÊîi,u½ZäÊounÊWVEàR_URàÇÇÇÊÊÊÊIäiîÊÒZ,ÑäX£½ZÎL,kîZ¾
                       ----------------------------------------------------
                        ''')
                input(f'\n\n\n{green}{player1.name}:{yellow}"What the hell is this?"')
                input(f'{green}{player1.name}:{yellow}"Before I kill the monster, the told me something."')
                input(f'{green}{player1.name}:{yellow}"Perhaps, this was the thing he was supposed to deliver to me."')
                input(f'{green}{player1.name}:{yellow}"I need to find out what this text means."{default}')
                break
            else:
                continue
        input('You put the paper to your pocket and then move on.')
        print(f"{blue}'Mysterious paper' {yellow}added to your puzzle box.{default}")
        puzzle_box.append(secret_message)
        input("You still can't figure out what was just happened between you and the monster.")
        input('The way he behave was so odd.')
        input('Among old trees, you are moving into the deepest of the forest.')
        input("...")
        chapter_one_complete = True
        clear()
        input(f"\n\n\t\t{blue}MENU ACCES AREA..")
        print(f'{red}(menu){default}: Whenever you see {red}(menu){default} at the beginning of a sentence, you can access to menu by\n typing {red}"m" {default}or {red}"menu"{default}. You can only access the menu when it is allowed.')
        while True:
            blabla = input(f"{red}(menu) {default}Come on try it.{red}'m'{default} to go to the menu.\n{red}(menu)Command:{default} ").lower()
            if blabla == 'm' or blabla == 'menu':
                clear()
                return take_action()
            clear()

    if chapter_one_complete == False:
        chapter_one()
    else:
        print(f"{green}You completed chapter 1.This is a demo. Try other options.{default}")


def take_action():
    global monster1

    while True:
        print(f"{blue}---------------------- Main Menu--------------------------------------")
        print(f'''{default}
            Type '{green}1{default}' or '{green}continue{default}' to continue to the game.
            Type '{green}2{default}' or '{green}wear{default}' to equip/take off your items.
            Type '{green}3{default}' or '{green}player info{default}'.
            Type '{green}4{default}' or '{green}inventory{default}' to see your inventory. 
            Type '{green}5{default}' or '{green}market{default}' to buy/upgrade/sell items.
            Type '{green}6{default}' or '{green}puzzle{default}' to see the puzzle.''')
        if operation_system == 'windows':
            print(f"\t    Type '{green}7{default}' to edit colors.")
        print(f'\t\t\t\tor their {green}first letters.{default}')
        action = input(f"{green}Main Menu-Take an action:{default} ").lower()
        if action == "wear" or action == 'w' or action == '2':
            return wear_item()
        elif action == "player info" or action == 'p' or action == '3':
            clear()
            player1.player_info()
        elif action == 'market' or action == 'm' or action == '5':
            clear()
            return market()
        elif action == "i" or action == "inventory" or action == '4':
            clear()
            display_player_inventory()
        elif action == "puzzle" or action == 'p' or action == '6':
            clear()
            return area_puzzle_box()
        elif action == "attack": #hikaye bitse bile rastgele yaratık çıkarıp dövüştür.
            clear()
            before_battle_prepare()
            in_battle()
            continue
        elif action == "continue" or action == 'c' or action == '1':
            clear()
            return play_game()
        elif action == '7':
            if operation_system == 'windows':
                print('I havent added the colors function yet.')
                input('')
                clear()
            else:
                clear()
                print(f"{red}\tInvalid command!{default}")
        else:
            clear()
            print(f"\t{red}Invalid command!{default}")


def display_player_inventory():
    print(f"{blue}---------------YOUR INVENTORY----------{default}")
    print(f"\t{yellow}Gold:{int(player1.gold)}{default}")
    b = 1
    memory_env_list = []
    for a in player_inventory:
        if a in memory_env_list:
            continue
        if a in equipped:
            if player_inventory.count(a) > 1:
                print(f"{yellow}{b}-)'{str(a).title()}' is equipped. x{player_inventory.count(a) - 1} left.{default}")
            else:
                print(f"{yellow}{b}-)'{str(a).title()}' is equipped.{default}")
        else:
            if player_inventory.count(a) > 1:
                if a == 'red pill' or a == 'blue pill':
                    print(f"{b}-)'{str(a).title()} x{player_inventory.count(a)}")
                else:
                    print(f"{default}{b}-)'{str(a).title()} x{player_inventory.count(a)}' is not equipped.{default}")
            else:
                if a == 'red pill' or a == 'blue pill':
                    print(f"{b}-)'{str(a).title()} x{player_inventory.count(a)}")
                else:
                    print(f"{default}{b}-)'{str(a).title()}' is not equipped.")
        memory_env_list.append(a)
        b += 1

    if len(equipped) < 0:
        for a in equipped:
            print(f"'{a.title()}")
    if len(player_inventory) == 0:
        print(f"\t\t{red}Unfortunately, you don't have any item yet1{default}")



def market():
    clear()

    def market_buy():

        while True:
            for key, value in string_item_prices.items():
                print(f"\t\t{default}'{key.title()}': {yellow}{value}.")
            print(f"{yellow}Your gold: {player1.gold}{default}")
            market_buy_input = input('Which item you want to buy: ').lower()
            if market_buy_input == "ok":
                return market()
            if market_buy_input == "m" or market_buy_input == 'menu':
                return take_action()
            elif market_buy_input not in item_tags:
                print(f"\t\t{red}Item '{market_buy_input}' does not exist!{default}")
                input(f'{magenta}\n\nPress anything to continue.{default}')
                clear()
                continue
            elif market_buy_input not in player_wearable:
                if "armor" in market_buy_input:
                    print(f"\t\t{red}You can't buy this armor.It's not suitable for your class!{default}")
                else:
                    print(f"{green}\t\tYou will not get full attributes from this item.Are you sure to buy? {blue}y/n{default}")
                    decisionbuy = input(f"{green}>>{default}").lower()
                    if decisionbuy == "y":
                        if player1.gold >= item_prices[market_buy_input]:
                            player1.gold -= item_prices[market_buy_input]
                            player_inventory.append(market_buy_input)
                            print(
                                f"\t\t{green}Item '{market_buy_input.title()}' added to your inventory.\n\t\tYour current gold is {yellow}{player1.gold}{default}")
                            input(f'{magenta}\n\nPress anything to continue.{default}')
                            clear()
                        elif player1.gold < item_prices[market_buy_input]:
                            print(
                                f"\t\t{red}Insufficient gold. You need '{yellow}{item_prices[market_buy_input] - player1.gold}{red}' more golds.{default}")
                            input(f'{magenta}\n\nPress anything to continue.{default}')
                            clear()
                            continue
                    else:
                        print(f"\t\t{green}Buying cancelled.{default}")
                        input(f'{magenta}\n\nPress anything to continue.{default}')
                        clear()
                        continue
            elif market_buy_input in player_wearable:
                decisionbuy = input(f"{magenta}Are you sure to buy?{yellow} y/n\n>{magenta}>>>>>{default}").lower()
                if decisionbuy == "y":
                    if player1.gold >= item_prices[market_buy_input]:
                        player1.gold -= item_prices[market_buy_input]
                        player_inventory.append(market_buy_input)
                        print(
                            f"\t\t{green}Item '{market_buy_input.title()}' added to your inventory.\n\t\tYour current gold is {yellow}{player1.gold}{default}")
                        input(f'{magenta}\n\nPress anything to continue.{default}')
                        clear()
                    elif player1.gold < item_prices[market_buy_input]:
                        print(
                            f"\t\t{red}Insufficient gold. You need '{yellow}{item_prices[market_buy_input] - player1.gold}{red}' more golds.{default}")
                        input(f'{magenta}\n\nPress anything to continue.{default}')
                        clear()
                        continue

    def market_attributes():
        for key, value in string_item_tags.items():
            print(f"'{key.title()}'{value}")
        input(f"{magenta}Press any button to move buy section.{default}")
        return market()

    def market_sell():
        global dwarf_sell_counter, asell_multiply
        if len(player_inventory) == 0:
            clear()
            print(f"{red}\t\tYou don't have any item!{default}")
            return take_action()

        while True:
            print(f"{blue}--------------------ITEM SELLING SECTION-------------------{default}")
            for a in player_inventory:
                print("'{0}' {1} Gold".format(a.title(), int(item_prices[a] * asell_multiply)))
            market_sell_input = input(f"{magenta}Which item to sell: {default}").lower()
            if market_sell_input == 'ok' or market_sell_input == 'm' or market_sell_input == 'menu':
                return take_action()
            if market_sell_input not in item_tags:
                print(f"\t{red}\tThis game doesn't have '{market_sell_input.title()}' item!{default}")
                clear()
                continue
            elif market_sell_input not in player_inventory:
                clear()
                print(f"\t\t{red}You don't have '{market_sell_input.title()}' item!{default}")
                continue
            elif market_sell_input in player_inventory:
                if market_sell_input in equipped:
                    clear()
                    print(f"\t\t{red}{market_sell_input.title()} is equipped. You need to take it off from inventory.{default}")
                    continue
                if market_sell_input not in equipped:
                    if user_race == "Dwarf":
                        if dwarf_sell_counter <= 0:
                            asell_multiply = 1
                            print(
                                f"\t{blue}You are no longer be able to sell your items with bonus. Your dwarf magic is over.")
                        dwarf_sell_counter -= 1
                        print(f"\t{green}You have {yellow}{dwarf_sell_counter} {green}chances left to sell item with bonus.{default}")

                    print(
                        f"\t{green}'{market_sell_input.title()}' is sold for {yellow}{int(item_prices[market_sell_input] * asell_multiply)}{green} gold.{default}")
                    player1.gold += item_prices[market_sell_input] * asell_multiply
                    player_inventory.remove(market_sell_input)
            else:
                print(
                    f"\n\n\n{red}Market sell place error.Honestly I set every condition but it seems i miss one. Can you please send a screenshot to aslanhassan98@gmail.com{default}")

    def market_upgrade():
        if len(player_inventory) == 0:
            clear()
            print(f"\t\t{red}You don't have any item!{default}")
            input(f'{magenta}\n\nPress anything to continue.{default}')
            return take_action()
        print(f"{blue}----------------------MARKET UPGRADE---------------------{default}")
        print(f"{yellow}\tGold:{int(player1.gold)}{default}")
        b = 1
        temporary_upgrade_display = []
        for a in player_inventory:
            if a in temporary_upgrade_display:
                continue
            if a in single_handed_list:
                print(
                    f"{blue}{b}-)'{str(a).title()}' \n\tPower: '{yellow}{item_tags[a]}{blue}' +-------> '{yellow}{int(item_tags[a] * 1.7 + 2)}{blue}', Cost: {yellow}{upgraded_item_price.get(a, str(700))} {blue}Gold.")
            elif a in double_handed_list:
                print(
                    f"{blue}{b}-)'{str(a).title()}' \n\tPower: '{yellow}{item_tags[a]}{blue}' +-------> '{yellow}{int(item_tags[a] * 1.9 + 3)}{blue}', Cost: {yellow}{upgraded_item_price.get(a, str(700))} {blue}Gold.")
            elif "armor" in a:
                print(
                    f"{blue}{b}-)'{str(a).title()}' \n\tHeal: '{yellow}{item_heals[a]}{blue}' +------->  '{yellow}{int(item_heals[a] * 1.7 + 2)}{blue}', Cost: {yellow}{upgraded_item_price.get(a, str(700))} {blue}Gold.")
                print(
                    f"\t{blue}Mana: '{yellow}{item_mana[a]}{blue}' +------->  '{yellow}{int(item_mana[a] * 1.7 + 2)}{blue}'{default}")
            elif "pill" in a:
                continue
            else:
                print("Market upgrade else section.")
            b += 1
            temporary_upgrade_display.append(a)
        upgrade_cost = 700
        if len(equipped) > 0:
            for a in equipped:
                print(f"'{a.title()}")
        print(f"\t{magenta}Each standart upgrade costs 700 gold.")
        if player1.gold < upgrade_cost:
            print(f"\t\t{red}Unfortunately you don't have enough gold.\nYou need {yellow}{upgrade_cost - player1.gold}{red} more golds.{default}")
            return market()
        while True:
            market_upgrade_input = input(f"{magenta}Which item to upgrade?{default}\n").lower()
            if market_upgrade_input == "ok":
                return market()
            if market_upgrade_input in upgraded_item_list:
                upgrade_cost = upgraded_item_price.get(market_upgrade_input)
            if "armor" in market_upgrade_input:
                store_itemhp = item_heals[market_upgrade_input]
                store_itemmana = item_mana[market_upgrade_input]
                multihp = item_heals[market_upgrade_input]
                multimana = item_mana[market_upgrade_input]
                multihp = int(multihp * 1.7 + 2)
                multimana = int(multimana * 1.7 + 2)
                new_upgrade_price = int(upgrade_cost * 1.3)
                print(f"\t\t{green}Next upgrade for this item will cost {yellow}{new_upgrade_price}{green} Gold.{default}")
                upgraded_item_list.append(market_upgrade_input)
                upgraded_item_price.update({market_upgrade_input: new_upgrade_price})
                item_heals.update({market_upgrade_input: multihp})
                item_mana.update({market_upgrade_input: multimana})
                player1.gold -= upgrade_cost
                print(
                    f"\t\t {player1.gold + upgrade_cost}-{upgrade_cost}={player1.gold} golds left.\n\t\tUpgrade completed.")
                print(
                    f"\t\t{green}New attributes: HP: {yellow}{item_heals[market_upgrade_input]}{green} MP: {yellow}{item_mana[market_upgrade_input]}{default}")
                input(f'{magenta}\n\nPress anything to continue.{default}')
                clear()
                if market_upgrade_input in equipped:
                    player1.heal_point += multihp - store_itemhp
                    player1.mana_point += multimana - store_itemmana
            elif "pill" in market_upgrade_input:
                print(f"{red}That item can't be upgraded!{default}")
                input(f'{magenta}\n\nPress anything to continue.{default}')
                clear()
                continue
            elif market_upgrade_input in item_tags:
                storeattack = item_tags[market_upgrade_input]
                multiattack = item_tags[market_upgrade_input]
                upgraded_item_list.append(market_upgrade_input)
                new_upgrade_price = int(upgrade_cost * 1.3)
                print(f"\t\t{green}Next upgrade for this item will cost {yellow}{new_upgrade_price}{green} Gold.{default}")
                upgraded_item_price.update({market_upgrade_input: new_upgrade_price})
                player1.gold -= upgrade_cost
                print(
                    f"\t\t{green} {yellow}{player1.gold + upgrade_cost}-{upgrade_cost}={player1.gold} {green}golds left.\n\t\tUpgrade completed.{default}")
                if market_upgrade_input in single_handed_list:
                    multiattack = int(multiattack * 1.7 + 2)
                elif market_upgrade_input in double_handed_list:
                    multiattack = int(multiattack * 1.9 + 3)
                item_tags.update({market_upgrade_input: multiattack})
                print(f"\t\t{green}New attributes: Attack Power: {yellow}{item_tags[market_upgrade_input]}{default}")
                input(f'{magenta}\n\nPress anything to continue.{default}')
                clear()
                if market_upgrade_input in equipped:
                    player1.power += multiattack
                    player1.fullpower -= storeattack
                    player1.fullpower = player1.power + player1.fullpower
                continue


            else:
                print(f"{red}\t\tNo item named '{market_upgrade_input}'{default}")

    while True:
        print(f"{blue}----------------------MARKET---------------------")
        print(f'''
                    Type '{yellow}1{blue}' to buy items.
                    Type '{yellow}2{blue}' to see the attributes.
                    Type '{yellow}3{blue}' to sell your items.
                    Type '{yellow}4{blue}' to upgrade your items.
                    Type '{yellow}5{blue}' or 'ok' or 'm' to return menu.{default}''')
        print(f"{blue}Your gold: {yellow}{player1.gold}{blue}. Your selling price rate:{yellow}{asell_multiply}{default}")
        market_input = input(f"{magenta}Enter your choice: {default}").lower()
        if market_input == '1' or market_input == 'price' or market_input == 'prices':
            clear()
            return market_buy()
        elif market_input == "ok" or market_input == 'm' or market_input == '5':
            clear()
            return take_action()
        elif market_input == '2' or market_input == 'attr':
            clear()
            return market_attributes()
        elif market_input == "3" or market_input == "sell":
            clear()
            return market_sell()
        elif market_input == "4" or market_input == "u" or market_input == "upgrade":
            clear()
            return market_upgrade()
        else:
            clear()
            print(f"\t\t{red}No such option!{default}")
            continue


def area_puzzle_box():
    print(decorators)
    print(f"{blue}----------------------PUZZLE---------------------")
    print(f"{green}You need to solve this mysteric message to find the secret you seek.")
    if len(puzzle_box) == 0:
        print(f"\t\t{red}You couldn't found any tip yet.{default}")
    else:
        print(f''' {green} You found {yellow}{len(puzzle_box)}{green} tips so far.\n\t\t\t\tMessage:\n\n\{default}
                        --------------------------------------------------
                       @O6iZ'ZäÊIo#6½uÊîi,u½ZäuÊu6isĞÎÊuZZÊ½iÊo½Ê½6k½Êo,
                       Ê½6ZÊ£äiÑZuuÊ6ZÊÎiZuÊ,i½ÊxZÑiîZÊkÊîi,u½ZäÇÊJ,ÎÊoI
                       ÊXisÊ#kZÊĞi,#ÊZ,is#6Êo,½iÊk,ÊkxXuunÊ½6ZÊkxXuuÊÀoĞĞÊ#
                       kZÊxkÑaÊo,½iÊXisÇ@Êf,Ê½6ZÊZ,ÎnXisÊäZkĞo/ZnÊ½6Z
                       ÊäZkĞÊîi,u½ZäÊounÊWVEàR_URàÇÇÇÊÊÊÊIäiîÊÒZ,ÑäX£½ZÎL,kîZ¾
                       ----------------------------------------------------\n
                        {blue}Letters:{yellow} {codex_alphabet_equal}''')
    while True:
        print(f"{blue}Type '{red}ok{blue}' or '{red}m{blue}' to return menu.{default}")
        puzzle_input = input(f"{magenta}Puzzle: {default}").lower()
        if puzzle_input == "m" or puzzle_input == "menu" or puzzle_input == 'ok':
            clear()
            return take_action()
        else:
            clear()
            print(f"\t{red}Puzzle is not responding. You need to solve all mysteries.{default}")


welcome_user()
take_action()
