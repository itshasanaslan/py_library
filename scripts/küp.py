def cubecode(base, power):
    result = 1
    for i in range(power):
        result = result * base
    return result


def cube():
    valid_input = False
    while not valid_input:
        base = input('Enter the base number: ')
        if base.lower() == "quit":
            print("You called an escape code. Quitting........")
            break
        power = input('Enter the power number: ')
        if power.lower() == "quit":
            print("You called an escape code. Quitting........")
            break
        if not (base.isnumeric() and power.isnumeric()):
            print('Please enter a number.')
        else:
            ### tek seferlik yapacaksam bu kodu yerleştircem valid_input = True
            base = int(base)
            power = int(power)
            print(cubecode(base, power))

cube()