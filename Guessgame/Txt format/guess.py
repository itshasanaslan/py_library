import datetime
import random

user = input("Hello. I am a basic gambler. And this is a guess game. What is your name?\n")
print("Nice to meet you " + str(user))
is_correct = False
a = 1
while a > 0:
    try:
        num1 = int(input("Tell me the minimum number you want.\n"))
        num2 = int(input("and the highest one.\n"))
        made = int(input("And how many chances you ask\n"))
        break
    ##############quit opsiyonu eksik.
    except:
        print("Enter a number please, not a string!")
if num1 < num2:
    numran = random.randint(num1, num2)
else:
    numran = random.randint(num2, num1)
guessesmade = 0

input("Okay. You have " + str(made) + " chances to guess the number between " + str(num1) + " and " + str(
    num2) + "\n Hit enter if it is clear")
while guessesmade < made:
    try:
        guess = int(input("Guess it.\n"))
        guessesmade += 1
        if guess < numran:
            print("No, it is higher.")
        if guess > numran:
            print("No. It is lower.")
        if guess == numran:
            break
    except:
        print("Enter a number please. ")
if guess == numran:
    is_correct = True
    print("Congratulations.You find my number trying only " + str(guessesmade) + " times!")
else:
    print("No " + str(user) + "! The number I think was " + str(numran))
    is_correct = False
if num1 == num2:
    print("But you did a cheat which I winked at :)")
my_record = open("guessrecord", "a")
my_record.readable()
my_record.write("\nUser: " + user + " -Numbers: " + str(num1) + "-" + str(num2) + " -Guesses asked: " + str(
    made) + " -Guesses used: " + str(guessesmade) + " -Did he guess correct: " + str(
    is_correct) + " -Correct number: " + str(numran) + " -Time: ")
my_record.write(str(datetime.datetime.now()))
my_record.close()
