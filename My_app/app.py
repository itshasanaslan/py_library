#en son, comment yaptıgın kod dizisini düzelt.Color manageer
# tüm hikayeyi yaz. Her canavaar ölürken konuşsun.
# canavar rastgele hp bassın güçlensin ya da zayıflasın.
# hangman guess game gibi puzlelar koy.

import random as r
import time
import os
import platform
from colorama import Style, Fore, init

init()
green = Style.BRIGHT + Fore.GREEN
blue = Style.BRIGHT + Fore.BLUE
red = Style.BRIGHT + Fore.RED
magenta = Style.BRIGHT + Fore.MAGENTA
yellow = Style.BRIGHT + Fore.YELLOW
default = Style.RESET_ALL
new_started = True


def windows_color_manager():
    print('Lo')
    time.sleep(0.8)
    clear()
    print('Load')
    time.sleep(0.8)
    clear()
    print(red,'Loading...')
    time.sleep(0.8)
    clear()
    input(f"{red}Press enter.{default}")
    input('You can pass every sentence by pressing enter.')
    input('Welcome...')
    input('Before starting, you may want to customize colours.')
    print('\tColor Optimizer')
    print(f'''    0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White	

    Color input must be given with two characters.
    First character = background color , Second character = foreground
    For ex: 0F = default background
    Type "{yellow}ok{default}" to exit.''')

    def color_welcome():
        list_memory = []
        memory = "012345678abcdefABCDEF"
        for a in memory:
            list_memory.append(a)
        for a in range(8):
            color1 = r.choice(list_memory)
            color2 = r.choice(list_memory)
            if color1 == color2:
                continue
            color_set = lambda: os.system(f'color {color1}')
            color_set()
            color_set = lambda: os.system(f'color {color2}')
            color_set()
            color_set = lambda: os.system(f'color {color1 + color2}')
            color_set()
            color_set = lambda: os.system(f'color {color2 + color1}')
            color_set()

        color_set = lambda: os.system(f'color 0f')
        color_set()

    def windows_color_input():
        color_checklist = []
        color_characters = "012345678abcdefABCDEF"
        for a in color_characters:
            color_checklist.append(a)
        while True:
            is_valid = True
            print(f"{red}WARNING! I STRONGLY RECOMMEND YOU NOT THE CHANGE COLORS! Type '{yellow}0F{red}' for default colors.")
            print(f"WARNING! I STRONGLY RECOMMEND YOU NOT THE CHANGE COLORS! Type '{yellow}0F{red}' for default colors.",default)
            color_input = input('Enter an option: ')
            if color_input == 'ok':
                if new_started:
                    break
                else:
                    return take_action()
            for a in color_input:
                if a not in color_checklist:
                    is_valid = False
            if is_valid:
                if len(color_input) > 2:
                    print('Enter a valid option!')
                    continue
                set_color = lambda: os.system(f'color {color_input}')
                set_color()

    color_welcome()
    windows_color_input()


operation_system = ""
if platform.system() == 'Linux':
    operation_system = 'linux'
    clear = lambda: os.system('clear')
elif platform.system() == 'windows' or platform.system() == 'Windows' or 'windows' in platform.system():
    operation_system = 'windows'
    clear = lambda: os.system(('cls'))
    clear()
    windows_color_manager()


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


def secret_codex():
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
    key_list = list(codex.keys())
    val_list = list(codex.values())
    while True:
        select_a_letter = r.choice(codex_alphabet)
        if select_a_letter in user_discovered_codex_alphabet:
            continue
        else:
            user_discovered_codex_alphabet.append(select_a_letter)
            break
    get_letter = codex.get(select_a_letter)
    secret_codex_text = select_a_letter + " = " + get_letter
    codex_alphabet_equal.append(secret_codex_text)
    puzzle_box.append(secret_codex_text)
    print("\n\tSystem: You found a new tip!")
    print(matrix(65))
    print('\n...')
    time.sleep(1)
    print("....")
    time.sleep(1)
    print("\tSystem: A secret revealed!")
    print(f"\n\t\t{secret_codex_text}")
    print("\n\tSystem: Your puzzle is updated.")
    input(f'{magenta}\n\nPress anything to continue.{default}')
    clear()


decorators = "----------------------------------------------------------------------"
dwarf_sell_counter = 5
warrior_item = (
    "single sword", "double sword", 'single axe', 'bow', 'ring', 'mighty ring', 'elven armor', 'warrior armor',
    'dwarf armor', 'aragorn armor', 'red pill', 'blue pill', 'shield', 'great shield')
dwarf_item = (
    'single sword', 'single axe', 'double axe', 'bow', 'ring', 'mighty ring', 'elven armor', 'warrior armor',
    'dwarf armor',
    'gimli armor', 'red pill', 'blue pill', 'shield')
elf_item = (
    'single sword', 'single axe', 'bow', 'mighty ring', 'ring', 'mighty bow', 'elven armor', 'warrior armor',
    'dwarf armor',
    'legolas armor', 'red pill', 'blue pill', 'shield', 'great shield')

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

single_handed_list = ("single sword", "shield", 'single axe', 'great shield')
double_handed_list = ('double sword', 'double axe', 'bow', 'mighty bow')

item_prices = {
    "aragorn armor": 2000,
    "legolas armor": 2400,
    'great shield': 1000,
    'double sword': 1000,
    "warrior armor": 550,
    "gimli armor": 3000,
    'mighty ring': 1420,
    'single sword': 500,
    'mighty bow': 1000,
    'double axe': 1000,
    "elven armor": 600,
    "dwarf armor": 700,
    'single axe': 500,
    "blue pill": 300,
    "red pill": 300,
    'shield': 600,
    'ring': 500,
    'bow': 500,
}

string_item_prices = {
    "aragorn armor": '  :   2000 Gold',
    "legolas armor": '  :   2400 Gold',
    'great shield': '   :   1000 Gold',
    'double sword': '   :   1000 Gold',
    "warrior armor": '  :   550  Gold',
    "gimli armor": '    :   3000 Gold',
    'mighty ring': '    :   1420 Gold',
    'single sword': '   :   500  Gold',
    'mighty bow': '     :   1000 Gold',
    'double axe': '     :   1000 Gold',
    "elven armor": '    :   600  Gold',
    "dwarf armor": '    :   700  Gold',
    'single axe': ':    :   500  Gold',
    "blue pill": '      :   300  Gold',
    "red pill": '       :   300  Gold',
    'shield': '         :   600  Gold',
    'ring': '           :   500  Gold',
    'bow': '            :   500  Gold'
}

string_item_tags = {
    "single sword": "   Gives '4' extra attack power.Warriors get +3 ",
    "single axe": "     Gives '4' extra attack power. ",
    "shield": "         Gives '4' extra attack power. Elves get +2",
    "great shield": "   Gives '7' extra attack power. Warriors get +3. ",
    "double sword": "   Gives '13' extra attack power.  ",
    "double axe": "     Gives '14' extra attack power. Dwarves get +2 ",
    "bow": "            Gives '4' extra attack power. Elves get +4",
    "mighty bow": "     Gives '10' extra attack power.",
    "ring": "           Gives '5' extra attack power. Elves get +3.",
    "mighty ring": "    Gives '10' extra attack power.If you are Dwarf, You will get +8.",
    "elven armor": "    Gives '90' heal points and '45' mana points.",
    "warrior armor": "  Gives '100' heal points and '60' mana points.",
    "dwarf armor": "    Gives '95' heal points and '45' mana points.",
    "aragorn armor": "  Gives '280' heal points and '200' mana points.",
    "legolas armor": "  Gives '240' heal points and '205' mana points.",
    "gimli armor": "    Gives '250' heal points and '190' mana points.",
    "red pill": "       Gives '50' heal points and '40' mana points for per level.",
    "blue pill": "      Gives '70' heal points and '60' mana points for per level."
}

item_tags = {
    "single sword": 4,
    "single axe": 4,
    "shield": 4,
    "great shield": 7,
    "double sword": 13,
    "double axe": 14,
    "bow": 4,
    "mighty bow": 10,
    "ring": 5,
    "mighty ring": 10,
    "elven armor": 0,
    "warrior armor": 0,
    "dwarf armor": 0,
    "aragorn armor": 0,
    "legolas armor": 0,
    "gimli armor": 0,
    "red pill": 0,
    "blue pill": 0
}

item_heals = {
    "elven armor": 90,
    "warrior armor": 100,
    "dwarf armor": 95,
    "aragorn armor": 280,
    "legolas armor": 240,
    "gimli armor": 250,
    "red pill": 50,
    "blue pill": 70
}

item_mana = {
    "elven armor": 45,
    "warrior armor": 60,
    "dwarf armor": 45,
    "aragorn armor": 200,
    "legolas armor": 205,
    "gimli armor": 190,
    "red pill": 40,
    "blue pill": 60
}

equipped = []
single_equipped = []
double_equipped = []
armor_equipped = []
player_inventory = []
upgraded_item_list = []
upgraded_item_price = {}


class Player:
    common_skill_manas = {"Iron Arrow": 0, "Silver Arrow": 0.15, "Call of Arwen": 0.20, "Forest Magic": 0.4,
                          'Soul Stealing': 0, 'Arken': 0.2, 'Athelas': 0.2, 'Whisper to the Dead': 0.4,
                          "Tenos": 0,
                          "Kalxelar": 0.2,
                          "Magic of Beard": 0.3,
                          "Madness": 0.6
                          }
    elf_skills = {
        "Iron Arrow": 1,  # standart attack
        "Silver Arrow": 1.20,  # standart
        "Call of Arwen": 1.3,  # gives attack and  heal
        "Forest Magic": 1.9  # standart
    }
    warrior_skills = {
        "Soul Stealing": 1,  # standart + heal
        "Arken": 1.6,  # standart
        "Athelas": 1.3,  # standart+heal
        "Whisper to the Dead": 2.4  # standart
    }
    dwarf_skills = {
        "Tenos": 0.7,  # heal, attack
        "Kalxelar": 1.7,  # attack
        "Magic of Beard": 2,  # attack
        "Madness": 1.8  # attack and heal
    }

    explain_elf_skills = {
        "Iron Arrow": "%100 damage. 0 MP.",
        "Silver Arrow": "%120 damage. -%15 MP.",
        "Call of Arwen": "%130 damage and %15 self-heal. -%20 MP.",
        "Forest Magic": "%190 damage. -%40 MP."
    }
    explain_warrior_skills = {
        "Soul Stealing": "%100 damage, 0 MP.",
        "Arken": "%160 damage. -%20 MP",
        "Athelas": "%130 damage amd %30 self-heal. -%20 MP.",
        "Whisper to the Dead": "Calling the dead and deals %240 damage. -%40 MP."
    }
    explain_dwarf_skills = {
        "Tenos": "%70 damage and %10 heal. 0 MP.",  # heal, attack
        "Kalxelar": "%170 damage. -%20 MP.",
        "Magic of Beard": "%200 damage. -%30 MP.",
        "Madness": "%220 damage. -%60 MP."
    }

    elf_skills_select_list = ["Iron Arrow", "Silver Arrow", "Call of Arwen", "Forest Magic"]
    warrior_skills_select_list = ['Soul Stealing', 'Arken', 'Athelas', 'Whisper to the Dead']
    dwarf_skills_select_list = ['Tenos', 'Kalxelar', 'Magic of Beard', 'Madness']

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.power = 0
        self.gold = 0

        self.fullpower = self.level + self.power

    def level_up(self):
        self.level += 1  # bunu yaratığın gücüne göre değişken verdir.
        input(f"\t{green}Level up! New level is {yellow}{self.level}.{default}")
        if user_race == "Elf":
            self.fullpower = 10 + self.level * 3 + 3
            self.fullpower += self.power
            self.mana_point += self.level * 50
            self.heal_point += self.level * 45
        elif user_race == "Warrior":
            self.fullpower = 10 + self.level * 4 + 5
            self.fullpower += self.power
            self.mana_point += self.level * 43
            self.heal_point += self.level * 45
        elif user_race == "Dwarf":
            self.fullpower = 7 + self.level * 3 + 4
            self.fullpower += self.power
            self.mana_point += self.level * 50
            self.heal_point += self.level * 45

    def player_race_optimize(self):
        if user_race == "Elf":
            self.heal_point = 100 + self.level * 45
            self.mana_point = 120 + self.level * 50
            self.gold = 350
            self.fullpower = 10 + self.level * 3 + 2
            self.skills_list = Player.elf_skills_select_list
            self.explain_skills_list = Player.explain_elf_skills
            self.skills_damage = Player.elf_skills
        elif user_race == "Warrior":
            self.fullpower += 10 + self.level * 4 + 3
            self.heal_point = 100 + self.level * 45
            self.mana_point = 90 + self.level * 43
            self.gold = 300
            self.skills_list = Player.warrior_skills_select_list
            self.explain_skills_list = Player.explain_warrior_skills
            self.skills_damage = Player.warrior_skills
        elif user_race == "Dwarf":
            self.mana_point = 140 + self.level * 50
            self.heal_point = 110 + self.level * 45
            self.fullpower += 7 + self.level * 3 + 2
            self.gold = 430
            self.skills_list = Player.dwarf_skills_select_list
            self.explain_skills_list = Player.explain_dwarf_skills
            self.skills_damage = Player.dwarf_skills

        print(
            f"\t{green}Player created!\n\n\t{blue}{user_race}\t\t{self.name}\n\n\t{red}Level: {yellow}{self.level}{red}\tItem Power: {yellow}{self.power}\n\n\t{red}Full Power: {yellow}{self.fullpower}\t{red}Heal Point: {yellow}{self.heal_point}\n\n\t{red}Mana Point: {yellow}{self.mana_point}\t{red}Gold: {yellow}{self.gold}{default}")
        self.in_battle_heal_point = 0
        self.in_battle_mana_point = 0
        self.skills_mana_cost = Player.common_skill_manas

    def player_info(self):
        print(
            f"\t{green}CHARACTER INFO\n\t{blue}{user_race}\t\t{self.name}\n\n\t{red}Level: {yellow}{self.level}{red}\tItem Power: {yellow}{self.power}\n\n\t{red}Full Power: {yellow}{self.fullpower}\t{red}Heal Point: {yellow}{self.heal_point}\n\n\t{red}Mana Point: {yellow}{self   .mana_point}\t{red}Gold: {yellow}{self.gold}{default}")

    def player_attack(self):
        while True:
            input("...")
            clear()
            print(f"\n\t{red}{monster1.name}, {blue}Level: {yellow}{monster1.level} \n\t{blue}HP: {yellow}{monster1.healpoint}, {blue}Power: {yellow}{monster1.power}")
            print(
                f"\n\t{magenta}{self.name}, {blue}Level: {yellow}{player1.level} \n\t{blue}HP: {yellow}{self.in_battle_heal_point} {blue}MP: {yellow}{self.in_battle_mana} {blue}Power: {yellow}{player1.fullpower}{default}")

            print(f"\t\t{green}SKILLS")
            c = 1
            for key, value in player1.explain_skills_list.items():
                print(yellow,str(c) + "-)"+blue+key, ":"+yellow, value)
                c += 1
            print(f"\n{magenta}Type '{red}r{magenta}' or '{blue}b{magenta}' to use {red}red pill {magenta}or {blue}blue pill{default}\n")
            skill_input = input(f'{magenta}Select a skill: ').lower()
            if skill_input == '1':
                that_skill = self.skills_list[0]
                if user_race == "Dwarf":
                    self.in_battle_heal_point += int(player1.heal_point * 0.10)
                    print(f"\t{red}System: {int(player1.heal_point * 0.10)} HP {yellow} is restored.{default}")
            elif skill_input == '2':
                that_skill = self.skills_list[1]
            elif skill_input == '3':
                that_skill = self.skills_list[2]
                if user_race == "Elf":
                    self.in_battle_heal_point += int(player1.heal_point * 0.15)
                    print(f"\t{red}System: {int(player1.heal_point * 0.15)} HP {yellow}is restored.{default}")
                elif user_race == "Warrior":
                    self.in_battle_heal_point += int(player1.heal_point * 0.30)
                    print(f"\t{red}System: {int(player1.heal_point * 0.30)} HP {yellow}is restored.{default}")
            elif skill_input == '4':
                that_skill = self.skills_list[3]
            elif skill_input == 'r':
                if 'red pill' not in player_inventory:
                    print(f"\t{red}System: You don't have any red pill.")
                    continue
                else:
                    player1.in_battle_heal_point += 50 * player1.level
                    player1.in_battle_mana_point += 40 * player1.level
                    print(
                        f"\t{red}System: Red pill {yellow}used. {blue}HP: {yellow}{player1.in_battle_heal_point} {blue}MP: {yellow}{player1.in_battle_mana_point}{default}")
                    continue
            elif skill_input == 'b':
                if 'blue pill' not in player_inventory:
                    print(f"\t{red}System: You don't have any {blue}blue pill.{default}")
                    continue
                else:
                    player1.in_battle_heal_point += 70 * player1.level
                    player1.in_battle_mana_point += 60 * player1.level
                    print(
                        f"\t{red}System: {blue}Blue pill {yellow}used. {blue}HP: {yellow}{player1.in_battle_heal_point} {blue}MP: {yellow}{player1.in_battle_mana_point}{default}")
                    continue
            else:
                print(f"{red}\tSystem: Please enter a valid skill number!{default}")
                continue
            self.mana_cost = int(self.skills_mana_cost[that_skill] * self.mana_point)
            critical_hit = r.randint(1, 3)
            if critical_hit == 2:
                critical_hit = r.randint(2, 3)
                print(f"\t{red}System: {green}CRITICAL HIT! YOU HIT THE HEAD!{default}")
            else:
                critical_hit == 1
            attack_multipler = self.skills_damage[that_skill] * critical_hit
            self.damage_attack = int(self.fullpower * attack_multipler)
            if self.in_battle_mana < self.mana_cost:
                print(f"\n\t{red}System: Your mana(skill point) is not enough!{default}")
                continue
            self.in_battle_mana -= self.mana_cost
            monster1.healpoint -= self.damage_attack
            if monster1.healpoint <= player1.fullpower:
                clear()
                while True:
                    random_sentence = r.choice(monstersentences)
                    if random_sentence in used_monstersentences:
                        if len(used_monstersentences) >= 6:
                            break
                        else:
                            continue
                    else:
                        used_monstersentences.append(random_sentence)
                        break
                print(f"{red}{monster1.name}: {yellow}{random_sentence}{default}")
                input(f'{magenta}...{default}')
                clear()
            if monster1.healpoint >= player1.fullpower:
                random_number = r.randint(0, 3)
                if random_number == 2:
                    clear()
                    while True:
                        random_sentence = r.choice(generic_monster_sentences)
                        if random_sentence in used_monstersentences:
                            if len(used_monstersentences) - 2 < len(used_monstersentences):
                                break
                            else:
                                continue
                        used_monstersentences.append(random_sentence)
                    print(f"{red}{monster1.name}: {yellow}{random_sentence}")
                    input('...')
                    clear()
            print(f"\t{red}System: {green}You gave {yellow}{self.damage_attack} {green}damage.{default}")
            break


class Monster:
    monster_names = ["Palotrix", "Othexus", "Dimpofsuax", "Resqulxalire"]
    adjectives = ["Outrageous", "Elder", "Mad", "Legendary", "Epic"]
    appeared_monsters = []

    Palotrix_skills_list = ["Basic Flame", "Mumbling Whistle", "Mad"]
    Palotrix_skills_attr = {"Basic Flame": 0.7, "Mumbling Whistle": 1.2, "Mad": 1.4}
    Palotrix_skills_explain = {"Basic Flame": "used her most basic skill.Apparently she is not minding this battle.",
                               "Mumbling Whistle": "It seem you made her a bit angry.",
                               "Mad": "Now she swore to destroy you!"}

    Othexus_skills_list = ["Lion-claw", "Deadly Whisper", "Sky Shout"]
    Othexus_skills_attr = {"Lion-claw": 1, "Deadly Whisper": 1.15, "Sky Shout": 1.3}
    Othexus_skills_explain = {"Lion-claw": "Basic but efficient.",
                              "Deadly Whisper": "He opens his mouth and inhaling deeply.",
                              "Sky Shout": "He looks at the sky for a few seconds. After a strong clench and inhale, he unleash the beast inside him."}

    Dimpofsuax_skills_list = ["Beast", "Thunder", "Nemrud's Mosquitos", "Call of Eire"]
    Dimpofsuax_skills_attr = {"Beast": 1, "Thunder": 1.1, "Nemrud's Mosquitos": 1.3, "Call of Eire": 1.4}
    Dimpofsuax_skills_explain = {"Beast": "the basic attack.", "Thunder": "like a Thor, but less efficient.",
                                 "Nemrud's Mosquitos": "such an enemy for one who is greedy!",
                                 "Call of Eire": "apparently, he is kin of Thor."}

    Resqulxalire_skills_list = ["Gritty Lawa", "Ingloriousness", "Lowness", "Poltroon"]
    Resqulxalire_skills_attr = {"Gritty Lawa": 1, "Ingloriousness": 1.2, "Lowness": 1.3, "Poltroon": 1.4}
    Resqulxalire_skills_explain = {"Gritty Lawa": "He open his hands and releases the grits and lawa.",
                                   "Ingloriousness": "the pure sign of evil.", "Lowness": "which is familiar.",
                                   "Poltroon": "which is unexpected!"}
    num_of_mons = 0

    def __init__(self):
        Monster.num_of_mons += 1
        while True:
            if player1.level in range(1, 4):
                self.adjective = Monster.adjectives[0]
            elif player1.level in range(4, 7):
                self.adjective = r.choice(Monster.adjectives[0:2], )
            elif player1.level in range(5, 9):
                self.adjective = r.choice(Monster.adjectives[0:3])
            elif player1.level in range(7, 12):
                self.adjective = r.choice(Monster.adjectives[0:4])
            elif player1.level >= 12:
                self.adjective = r.choice(Monster.adjectives)
            self.secondname = r.choice(Monster.monster_names)
            self.name = self.secondname + " The " + self.adjective
            if self.name in Monster.appeared_monsters:
                if len(Monster.appeared_monsters) <= 20:
                    self.secondname = r.choice(Monster.monster_names)
                    self.name = self.secondname + " The " + self.adjective
                    continue

            Monster.appeared_monsters.append(self.name)
            self.power = 1
            self.healpoint = 1
            self.level = 1
            break

    def monster_create(self):
        if self.secondname == "Palotrix":
            if player1.level <= 1:
                self.level = player1.level + r.randint(0, 1)
            else:
                self.level = player1.level + r.randint(-1, +4)
            self.power = self.level * 10
            self.healpoint = self.power * 4
            self.skills_list = Monster.Palotrix_skills_list
            self.skills_attr = Monster.Palotrix_skills_attr
            self.skills_explain = Monster.Palotrix_skills_explain
        elif self.secondname == "Othexus":
            if player1.level <= 1:
                self.level = player1.level + r.randint(0, 1)
            else:
                self.level = player1.level + r.randint(0, 1)
            self.power = self.level * 12
            self.healpoint = self.power * 5
            self.skills_list = Monster.Othexus_skills_list
            self.skills_attr = Monster.Othexus_skills_attr
            self.skills_explain = Monster.Othexus_skills_explain
        elif self.secondname == "Dimpofsuax":
            if player1.level <= 1:
                self.level = player1.level + r.randint(0, 1)
            else:
                self.level = player1.level + r.randint(-1, +4)
            self.power = self.level * 13
            self.healpoint = self.power * 6
            self.skills_list = Monster.Dimpofsuax_skills_list
            self.skills_attr = Monster.Dimpofsuax_skills_attr
            self.skills_explain = Monster.Dimpofsuax_skills_explain
        elif self.secondname == "Resqulxalire":
            if player1.level <= 1:
                self.level = player1.level + r.randint(0, 1)
            else:
                self.level = player1.level + r.randint(-1, +4)
            self.power = self.level * 14
            self.healpoint = self.power * 7
            self.skills_list = Monster.Resqulxalire_skills_list
            self.skills_attr = Monster.Resqulxalire_skills_attr
            self.skills_explain = Monster.Resqulxalire_skills_explain
        if self.adjective == "Outrageous":
            self.power *= int(1)
            self.healpoint *= int(1)
        elif self.adjective == "Elder":
            self.power *= int(1.2)
            self.healpoint *= int(1.2)
        elif self.adjective == "Mad":
            self.power *= int(1.5)
            self.healpoint *= int(1.5)
        elif self.adjective == "Legendary":
            self.power *= int(1.8)
            self.healpoint *= int(1.8)
        elif self.adjective == "Epic":
            self.power *= 2
            self.healpoint *= 2
        print(f"\t\t{red}{self.name} is appeared.\n\t\t{red}Level: {yellow}{self.level}{red} Power: {yellow}{self.power} {red}HP: {yellow}{self.healpoint}{default}\n")
        self.total_damage_give = 0
        self.monster_dead = False

    def attack(self):
        input("...")
        attacked_list = []
        attack = r.choice(self.skills_list)
        while not self.monster_dead:
            attack = r.choice(self.skills_list)
            if attack in attacked_list and len(attacked_list) == len(self.skills_list):
                break
            elif attack in attacked_list and len(attacked_list) < len(self.skills_list):
                continue
            else:
                attacked_list.append(attack)
                break
        damage = int(self.power * self.skills_attr[attack])
        print(f"\t{red}System: {green}{self.name} uses '{yellow}{attack}{green}' skill and gave you {yellow}{damage}{green} damage.{default}")
        player1.in_battle_heal_point -= damage
        if player1.in_battle_heal_point < 0:
            print(f"\t{red}System:{green} You died.{green}")
            game_over()
            return play_game()

    # en sona adjective a göre gold ekle.
    def drop_item(self):
        dropitem = r.choice(whole_item_control)
        gold = 100
        if self.level in range(1, 5):
            gold = r.randint(50, 150)
            chance = r.randint(1, 10)
            if chance == 5:
                templist = ['single sword', 'single axe', 'bow']
                dropitem = r.choice(templist)
        elif self.level in range(5, 8):
            gold = r.randint(150, 300)
            templist = ['dwarf armor', 'elven armor', 'warrior armor']
            dropitem = r.choice(templist)
        elif self.level in range(8, 1000):
            gold = r.randint(200, 3000)
            dropitem = r.choice(whole_item_control)
        if self.adjective == Monster.adjectives[1]:
            gold += r.randint(100, 400)
        elif self.adjective == Monster.adjectives[2]:
            gold += r.randint(250, 500)
        elif self.adjectives == Monster.adjectives[3]:
            gold += r.randint(500, 1000)
        elif self.adjectives == Monster.adjectives[4]:
            gold += r.randint(1000, 3000)
            templist = ['aragorn armor', 'legolas armor', 'gimli armor']
            dropitem = r.choice(templist)
        pills = ['blue pill', 'red pill']
        dropitem2 = r.choice(pills)
        dropitemchance = r.randint(1, 2)
        player_inventory.append(dropitem)
        player_inventory.append(dropitem2)
        if dropitemchance == 2:
            player_inventory.append(dropitem2)
        input(f"\t{red}System: {yellow}'{dropitem.title()}{default}' and '{yellow}{dropitem2.title()} x{dropitemchance}'{green} added to your inventory.{default}")
        input(f"\t{red}System: {yellow}'{gold} Gold'{green} added to your pocket.")
        player1.gold += gold


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


def wear_item():
    clear()
    if len(player_inventory) == 0:
        print(f"\t\t{red}You don't have any item yet.Try '{yellow}market{red}'{default}")
        return take_action()
    print(f"{blue}---------------------- WEAR ITEM-----------------------{default}\n\t\tType '{red}ok{default}' to return menu. '{red}remove{default}' to take off an item you equipped.")
    while True:
        input("..")
        clear()
        display_player_inventory()
        print(f"\n{magenta}Available commands:'{yellow}ok{magenta}', '{yellow}m{magenta}', '{yellow}remove{magenta}', '{yellow}inventory{magenta}'\n")
        wear_input = input(f"\n{magenta}Which item you want to wear: {default}").lower()
        if wear_input == "info":
            player1.player_info()
            continue
        if wear_input == "ok":
            clear()
            return take_action()
        elif wear_input == "inventory" or wear_input == 'i':
            display_player_inventory()
            continue
        elif wear_input == "m" or wear_input == 'menu':
            clear()
            return take_action()
        elif wear_input == "remove" or wear_input == 'r':
            return remove_item()
        elif wear_input not in item_tags:
            print(f"{red}\t\tNo such item!{default}")
            continue
        elif wear_input in equipped:
            print(f"{red}\t\tItem '{wear_input.title()}' already equipped!")
            input(f'{magenta}\n\nPress anything to continue.{default}')
            continue
        elif wear_input not in player_inventory:
            print(f"\t\t{red}You don't have '{wear_input.title()}' item.")
            input(f'{magenta}\n\nPress anything to continue.{default}')
            continue
        elif 'ring' in wear_input:
            equipped.append(wear_input)
            print(f"\t\t{green}'{wear_input.title()}' is equipped{default}")
            player1.power += item_tags.get(wear_input)
            input(f'{magenta}\n\nPress anything to continue.{default}')
            clear()
            continue
        elif wear_input not in player_wearable:
            if "armor" in wear_input:
                print(f"\t\t{red}This armor is not suitable for you.{default}")
                continue
            else:
                if wear_input in single_handed_list and len(single_equipped) == 0 and len(double_equipped) == 0:
                    equipped.append(wear_input)
                    single_equipped.append(wear_input)
                    player1.fullpower -= player1.power
                    player1.power += item_tags[wear_input]
                    player1.fullpower += player1.power
                    print(f"\t\t{green}'{wear_input.title()}' is equipped.{default}")

                elif wear_input in double_handed_list and len(single_equipped) == 0 and len(double_equipped) == 0:
                    print(f"\t\t{red}It is not suitable for you. So I decrease 5 power points.{default}")
                    equipped.append(wear_input)
                    double_equipped.append(wear_input)
                    item_tags[wear_input] -= 5
                    player1.fullpower -= player1.power
                    player1.power += item_tags[wear_input]
                    player1.fullpower += player1.power
                    print(f"\t\t{green}'{wear_input.title()}' is equipped.{default}")
                elif wear_input in single_handed_list and len(single_equipped) == 1 and len(double_equipped) == 0:
                    equipped.append(wear_input)
                    single_equipped.append(wear_input)
                    player1.fullpower -= player1.power
                    player1.power += item_tags[wear_input]
                    player1.fullpower += player1.power
                    print(f"\t\t{green}'{wear_input.title()}' is equipped.{default}")
                else:
                    print(f"\t\t{red}You can only carry one double handed or 2 single handed weapon at same time!{default}")
                    continue
        elif wear_input in player_wearable:
            if "pill" in wear_input:
                if wear_input in player_inventory:
                    global player_health_wo_pills, player_mana_wo_pills
                    player_health_wo_pills = player1.heal_point
                    player_mana_wo_pills = player1.mana_point
                    for b in equipped:
                        if b in item_heals:
                            player1.heal_point += item_heals[b]
                        if b in item_mana:
                            player1.mana_point += item_mana[b]

                    print(f"{green}\t\tPure heal is {player_health_wo_pills}, pure mana {player_mana_wo_pills}{default}")
                    player1.heal_point += item_heals[wear_input]
                    player1.mana_point += item_mana[wear_input]
                    player_inventory.remove(wear_input)
                    print(f"{green}\t\tYour current heal is {yellow}{player1.heal_point}. {green}Your mana point is {yellow}{player1.mana_point}{default}")
                    continue
                else:
                    print(f"\t\t{red}You don't have any pills!{default}")
            elif wear_input in equipped:
                print(f"\t\t{red}Item '{wear_input.title()}' already equipped!{default}")
                continue
            elif "armor" in wear_input:
                if len(armor_equipped) > 0:
                    print(f"\t\t{red}You need to take off '{armor_equipped[0]}'{default}")
                    continue
                armor_equipped.append(wear_input)
                equipped.append(wear_input)
                player1.heal_point += item_heals[wear_input]
                player1.mana_point += item_mana[wear_input]
                print(f"\t\t{green}'{wear_input.title()}' is equipped.{default}")
                print(f"\t\t{green}Your current heal is{yellow} {player1.heal_point}{green}. Your mana point is {yellow}{player1.mana_point}{default}")
            else:
                if wear_input in single_handed_list and len(single_equipped) == 0 and len(double_equipped) == 0:
                    equipped.append(wear_input)
                    single_equipped.append(wear_input)
                    player1.fullpower -= player1.power
                    player1.power += item_tags[wear_input]
                    player1.fullpower += player1.power
                    print(f"\t\t{green}'{wear_input.title()}' is equipped{default}")

                elif wear_input in double_handed_list and len(single_equipped) == 0 and len(double_equipped) == 0:
                    equipped.append(wear_input)
                    double_equipped.append(wear_input)
                    player1.fullpower -= player1.power
                    player1.power += item_tags[wear_input]
                    player1.fullpower += player1.power
                    print(f"{green}\t\t'{wear_input.title()}' is equipped{default}")
                elif wear_input in single_handed_list and len(single_equipped) == 1 and len(double_equipped) == 0:
                    equipped.append(wear_input)
                    single_equipped.append(wear_input)
                    player1.fullpower -= player1.power
                    player1.power += item_tags[wear_input]
                    player1.fullpower += player1.power
                    print(f"{green}\t\t'{wear_input.title()}' is equipped{default}")
                else:
                    print(f"{red}\t\t You can only carry one double handed or 2 single handed weapon at same time!{default}")
                    continue


def remove_item():
    if len(player_inventory) == 0:
        print(f"\t\t{red}You don't have any item!{default}")
        input(f'{magenta}\n\nPress anything to continue.{default}')
        clear()
        return wear_item()
    elif len(equipped) == 0:
        print(f"{red}\n\t\tYou are not wearing any item!\n{default}")
        input(f'{magenta}\n\nPress anything to continue.{default}')
        clear()
        return wear_item()

    while True:
        clear()
        print(f"{blue}---------------------- REMOVE ITEM-----------------------{default}")
        print(f"\t\t{yellow}Here you can take off your items. They will stay in your inventory till you equip or sell them.{default}")
        print(f"{magenta}Available commands: '{yellow}ok{magenta}', '{yellow}menu{magenta}' or '{yellow}m{magenta}'{default}\n")
        remove_input = input(f"{magenta}Which item you want to remove: {default}").lower()
        if remove_input == "ok":
            return wear_item()
        elif remove_input == "info":
            player1.player_info()
            continue
        elif remove_input == "bla":
            print("bla")
        elif remove_input == "inventory":
            display_player_inventory()
            input(f'{magenta}\n\nPress anything to continue.{default}')
            continue
        elif remove_input not in item_tags:
            print(f"{red}\t\tNo such item!{default}")
            input(f'{magenta}\n\nPress anything to continue.{default}')
            continue
        elif remove_input not in equipped:
            print(f"{red}\t\tYou weren't wearing that item.{default}")
            input(f'{magenta}\n\nPress anything to continue.{default}')
            continue
        elif remove_input not in player_wearable and remove_input in equipped:
            print(f"{green}\t\tIt wasn't fitting you anyway.{default}")
            if remove_input in double_equipped:
                double_equipped.remove(remove_input)
            elif remove_input in single_equipped:
                single_equipped.remove(remove_input)
            player1.fullpower -= player1.power
            player1.power -= item_tags[remove_input] - 5
            player1.fullpower += player1.power
            equipped.remove(remove_input)
            print(f"{blue}\t\t'{remove_input}' is removed.{default}")
        elif remove_input in player_wearable and remove_input in equipped:
            if 'armor' in remove_input:
                armor_equipped.remove(remove_input)
                print(f"{blue}\t\t'{remove_input.title()}' is removed.{default}")
                player1.heal_point -= item_heals[remove_input]
                player1.mana_point -= item_mana[remove_input]
                equipped.remove(remove_input)
                print(
                    f"\t\t{green}Your current heal point is {yellow}{player1.heal_point}{green}.Your current mana point is {yellow}{player1.mana_point}{default}")
            else:
                if remove_input in single_equipped:
                    single_equipped.remove(remove_input)
                elif remove_input in double_equipped:
                    double_equipped.remove(remove_input)
                player1.fullpower -= player1.power
                player1.power -= item_tags[remove_input]
                player1.fullpower += player1.power
                print(f"{blue}\t\t'{remove_input}' is removed{default}")
                equipped.remove(remove_input)
                print(f"\t\t{green}Your current power is {yellow}{player1.fullpower}{default}")
                input(f'{magenta}\n\nPress anything to continue.{default}')


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
