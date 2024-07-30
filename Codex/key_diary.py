from pathlib import Path
from colorama import Style, Fore
import os

mypath = Path()

my_list = []
for a in mypath.glob('*'):
	a = str(a)
	for b in a:
		if b in '0123456789':
			my_list.append(a)
			break

myfile = my_list[0]

ec_filename = 'decrypted_text+++.txt'
green = Style.BRIGHT + Fore.GREEN
blue = Style.BRIGHT + Fore.BLUE
red = Style.BRIGHT + Fore.RED
magenta = Style.BRIGHT + Fore.MAGENTA
password = '8448209aAlog'

enter_pass = input('Enter your password: ')
if enter_pass!=password:
    os.system('python3 /alert_diary.py')
    print('Please leave.')
    quit()

os.system('clear')

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
print(magenta + '''Welcome! This function encrypts-decrypts your text.''')


def codex_file_process():
    while True:
        os.system('clear')
        print('''
        		Type 1 to encrypt
        		Type 2 to decrypt''')
        try:
            codex_process = input(blue + ">>>")
            if codex_process == "see files":
                for file in mypath.glob("*"):
                    print(green + str(file))
                continue
            elif codex_process == "menu":
                return codex_menu()
            elif codex_process not in "12":
                print("Please enter a valid operation. 1,2 or 3")
                continue
            elif codex_process == "1":
                codex_file_input = myfile
                if codex_file_input == "menu":
                    quit()
                codex_file_output = ""
                with open(codex_file_input) as f:
                    codex_file_text = f.read()
                    for letter in codex_file_text:
                        codex_file_output += codex.get(letter,letter)
                en_filename = codex_file_input
                with open(en_filename, 'w') as ff:
                    ff.write(codex_file_output)
                input(f"\t\t\tYour encrypted text saved to {en_filename} in your directory.")
            elif codex_process == "2":
                codex_file_input = myfile
                if codex_file_input == "menu":
                    quit()
                codex_file_output = ""
                with open(codex_file_input) as f:
                    codex_file_text = f.read()
                    for letter in codex_file_text:
                        codex_file_output += key_list[val_list.index(letter)]
                dec_filename = codex_file_input[:2]
                with open(dec_filename, 'w') as ff:
                    ff.write(codex_file_output)
                input(f"\t\t\tYour decrypted text saved to {dec_filename} in your directory.")
        except ValueError:
            print(f"{red}This character might not be assigned sir: {letter} ")
        except Exception as codex_file_exception:
            print(red + str(codex_file_exception))
codex_file_process()