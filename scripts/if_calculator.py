operators = ["+", "-", "*", "/", "**"]
is_continue = True
print('''This is a simple calculator. Enter the first number and then hit
enter. Then enter the second number. Finally enter an operator.
+ addition
- subtraction
* multiply
/ division
** power''')
while is_continue:
    num1 = input("First number:  ")
    if num1.lower() == "quit":
        print("Quitting.")
        break
    elif not num1.isnumeric():
        print("Enter a number please.")
        continue
    num2 = input("Second number:  ")
    if num2.lower() == "quit":
        print("Quitting.")
        break
    elif not num2.isnumeric():
        print("Enter a number please.")
        continue
    opcho = input("Operator:  ")
    if opcho.lower() == "quit":
        print("quitting.")
        break
    elif opcho not in operators:
        print("Enter a correct operator: + - * /")
        continue
    if operators[0] in opcho:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
        print("Result is: " + str(num1) + "+" + str(num2) + "=" + str(result))
    elif operators[1] in opcho:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 - num2
        print("Result is: " + str(num1) + "-" + str(num2) + "=" + str(result))

    elif operators[3] in opcho:
        num1 = int(num1)
        num2 = int(num2)
        try:
            result = num1 / num2
            print("Result is: " + str(num1) + "/" + str(num2) + "=" + str(result))
        except ZeroDivisionError:
            print("Error. Can't divide with 0")
    elif opcho == "**":
        num1 = int(num1)
        num2 = int(num2)
        result = num1 ** num2
        print("Result is: " + str(num1) + "**" + str(num2) + "=" + str(result))
    elif operators[2] in opcho:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 * num2
        print("Result is: " + str(num1) + "*" + str(num2) + "=" + str(result))
