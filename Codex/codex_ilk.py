from pathlib import Path
from colorama import Style, Fore

mypath = Path()
en_filename = 'encrypted_text+++.txt'
dec_filename = 'decrypted_text+++.txt'
green = Style.BRIGHT + Fore.GREEN
blue = Style.BRIGHT + Fore.BLUE
red = Style.BRIGHT + Fore.RED
magenta = Style.BRIGHT + Fore.MAGENTA


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
        "Q": "ó", "_": "L", "&": "ü", "=": ";", "å": "0", "ò": "İ", "ù": "á",
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

    def codex_encrypt():
        print(magenta + "             Encryption Section\n", green + "            Type 'menu' to return")
        while True:
            codex_user_input = input(blue + "Enter your text: ")
            codex_encrypted_output = ""
            if codex_user_input == "q":
                print(magenta + "         Leaving encryption section")
            elif codex_user_input == "menu":
                return codex_menu()
            try:
                for a in codex_user_input:
                    codex_encrypted_output += codex.get(a,a)
                print(f"{green}Here is your encrypted text: {codex_encrypted_output}")
            except Exception as codex_except:
                print(red + str(codex_except))
                continue

    def codex_decrypt():
        print(magenta + "             Decryption Section\n", green + "            Type 'menu' to return")
        while True:
            codex_user_input = input(blue + "Enter your text: ")
            codex_decrypted_output = ""
            if codex_user_input == "q":
                print(magenta + "         Leaving decryption section")
                break
            elif codex_user_input == "menu":
                return codex_menu()
            try:
                for b in codex_user_input:
                    codex_decrypted_output += key_list[val_list.index(b)]
                print(f"{green}Here is your decrypted text: {codex_decrypted_output}")
            except Exception as codex_except:
                print(red + (codex_except))
                continue

    def codex_file_process():
        print(magenta + "File Encryption/Decryption Section")
        print('''\tType "1" to encrypt\n\tType "2" to decrypt\n\tType "see files" to see the files in the directory''')
        while True:
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
                    codex_file_input = input("Enter a filename to encrypt: ")
                    if codex_file_input == "menu":
                        return codex_menu()
                    codex_file_output = ""
                    with open(codex_file_input) as f:
                        codex_file_text = f.read()
                        for letter in codex_file_text:
                            codex_file_output += codex.get(letter,letter)
                    with open(en_filename, 'w') as ff:
                        ff.write(codex_file_output)
                    print(f"\t\t\tYour encrypted text saved to {en_filename} in your directory.")
                elif codex_process == "2":
                    codex_file_input = input("Enter a filename to decrypt: ")
                    if codex_file_input == "menu":
                        return codex_menu()
                    codex_file_output = ""
                    with open(codex_file_input) as f:
                        codex_file_text = f.read()
                        for letter in codex_file_text:
                            codex_file_output += key_list[val_list.index(letter)]
                    with open(dec_filename, 'w') as ff:
                        ff.write(codex_file_output)
                    print(f"\t\t\tYour decrypted text saved to {dec_filename} in your directory.")
            except ValueError:
                print(f"{red}This character might not be assigned sir: {letter} ")
            except Exception as codex_file_exception:
                print(red + str(codex_file_exception))

    def codex_menu():
        print(
            '''            Type '1' to encrypt text\n            Type '2' to decrypt text\n            Type '3' to encrypt/decrypt file''')
        while True:
            codex_menu_input = input(blue + ">>> ")
            if codex_menu_input == "q":
                print(red + "Escaping.. See you sir!")
                break
            else:
                try:
                    if codex_menu_input == "1":
                        return codex_encrypt()
                    elif codex_menu_input == "2":
                        return codex_decrypt()
                    elif codex_menu_input == "3":
                        return codex_file_process()
                    else:
                        print(red + "Please enter a valid operation. 1,2 or 3")
                        continue
                except Exception as codex_menu_exception:
                    print(codex_menu_exception)

    codex_menu()


secret_codex()
