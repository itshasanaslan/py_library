from string import digits, punctuation
import os

def pasvalidator():
    while True:
        is_spe = False
        is_numeric = False
        space_check = False
        len_check = False
        input()
        os.system('cls')
        pswd = input("Enter your password:  ")
        if not 5 <= len(pswd) <= 10:
            print("It must be between 5-10 characters!")
        else:
            len_check = True
        if " " in pswd:
            space_check = False
            print("You are not allowed to use spaces!")
        else:
            space_check = True
        if not any(c in digits for c in pswd):
            print("At least  one number should be included")
        else:
            is_numeric = True
        for a in pswd:
            if a in "+-*/&%^'!#£><½¾{[}[{¾-|_":
                is_spe = True
        if is_spe and is_numeric and space_check and len_check:
            print("Done! Your password is:", pswd)
            break
        if not is_spe:
            print("You need to use at least one special character! ;+-*/&%^'!#£><½¾{[}[{¾-|_")


pasvalidator()
