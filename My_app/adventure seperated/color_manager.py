from colorama import Style, Fore, init
init()
green = Style.BRIGHT + Fore.GREEN
blue = Style.BRIGHT + Fore.BLUE
red = Style.BRIGHT + Fore.RED
magenta = Style.BRIGHT + Fore.MAGENTA
yellow = Style.BRIGHT + Fore.YELLOW
default = Style.RESET_ALL
new_started = True



clear = lambda:os.system('cls')
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

