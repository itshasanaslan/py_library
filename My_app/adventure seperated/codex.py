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