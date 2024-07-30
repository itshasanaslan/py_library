def my_guide():
    print('''
                                    fonksiyonlar ve isimleri:
    
    advcalc()                       en iyi calculatorum\n
    agent_number_code()             kod kırma oyunu\n
    calculate_money_currency()      para birimi dönüştürücü\n
    calculator_basic()              basit calculatorum\n
    cube()                          sayını küpünü verir\n
    file_caller                     verdiğim isimde dosya varsa içindekileri yazar yoksa oluşturur\n
    keygen()                        5 basamaklı key generate eder.\n
    letter_combination()            Harf kombinasyonları üretir.\n
    mail_validator()                E-mail adresi girdisi alır.
    matrix()                        matrix animasyonu\n
    neo(default neo)                White rabbit\n
    number_generator()              Rastgele sayı dizisi üretir.\n
    pas_validator()                 password doğrulama\n
    prime_nums                      Asal sayı\n
    prime_limit()                   Verdiğim limite kadar olan asal ve asal olmayan sayıları gösterir\n
    print(factorial(x))             faktöriyel\n
    print(fib(x))                   fibonacci\n
    random_math()                   Rastgele matematik soruları üretir.\n
    rock_paper_scissor()            Taş kağıt makas oyunu\n
    statistics()                    İstatistik\n
    Student                         isminde bir class. myfunc = sayhello\n     
    sum_to_limit                    verdiğim sayıya kadar olan sayıların toplamını verir\n
    summations_calculator()         Range hesaplaması.\n
    tc_ilkdokuz()                   T.C. no son 2 haneyi verir.\n
    tc_validate()                   Verdiğim T.C.nin algoritmasını inceler.\n
    turkish_character()             Verdiğim cümledeki karakterleri kontrol eder. \n
    
    ''')


#####################################################333
class Student:  ###Student sınıfım
    def __init__(self, name, surname, is_on_probation, gpsa):
        self.name = name
        self.surname = surname
        self.is_on_probation = is_on_probation
        self.gpsa = gpsa

    def myfunc(self):
        print("Hello! My name is " + self.name + self.surname + "My gpsa is " + str(self.gpsa))

    def on_honor_roll(self):
        if self.gpsa >= 3.5:
            return True
        else:
            return False


class Questions:  ##quiz şeysi
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def __str__(self):
        return (str(self.prompt) + str(self.answer))


## calculatorbasic, cube, advcalc
def calculator_basic():
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


############################################################################################

def cubecode(base, power):  ### bu ve alttaki birleşik
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


############################################################################################
def advcalc():
    checklist = "0123456789+-/*="
    inputcheck = False
    print("""
    This is a simple calculator.
    Operations: / to Divide
            * to Multiply
            + to Add
            - to Substract
            ** to get power number
    Just write the operation and hit the enter Ex: 764+232""")
    while True:
        userdata = input("Enter the operation: ")
        if userdata.lower() == "q":
            print("You called an escape code. Leaving...")
            break
        for a in userdata:
            if a not in checklist:
                print("Wrong characters. Only use 0 1 2 3 4 5 6 7 8 9 + - / * = ")
            continue
        print("Result is : " + str(eval(userdata)))


############################################################################################
######Password Validator
from string import digits, punctuation


def pas_validator():
    from string import digits, punctuation
    while True:
        is_spe = False
        is_numeric = False
        space_check = False
        len_check = False
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


############################################################################################
############################Asal Sayı######################################################
def prime_nums():
    print(
        "Çıkmak için herhangi bir harf yazmam yeterli.\n Bir sayı sadece 1'e ve kendisine bölünebiliyorsa asal sayıdır")
    is_prime = False
    while True:
        is_prime = False
        try:
            x = int(input(">>>>"))
        except:
            print("See you bro.")
            break
        if x < 2:
            print("Minimum number is 2!")
            continue
        elif x == 2:
            print("2 is the first prime number!")
        if x >= 2:
            for i in range(2, x):
                if x % i == 0:
                    print(f'{x} is not a prime number.\n{x / i} times {i} ==== {x}')
                    is_prime = False
                    break
                else:
                    is_prime = True
        if is_prime:
            print(f"{x} is a prime number!")


########################################################################################################
###########################Fibonacci Sayıları, 1,1,2,3,5,8,13,21 bir önceki sayıyla toplanarak gider.########print(fib(x))
def fib(x):
    if x <= 1:
        return x
    else:
        return fib(x - 1) + fib(x - 2)


#########################################################################################################
##################### Faktöriyel############3
def factorial(x):
    if x <= 1:
        return x
    else:
        return x * factorial(x - 1)


############################################################################################################
## verdiğim limite kalan olan sayılardan 3 ve 5 in katların alarak toplamını verir.##
def sum_to_limit(x):
    arra = []
    for a in range(x + 1):
        b, c = a * 3, a * 5
        if b <= x and b not in arra:
            arra.append(b)
        if c <= x and c not in arra:
            arra.append(c)
    print(arra,sep =" ")

    print(
        f"This function takes the sum of all numbers that is multiples of 3 and 5 until reaches your limit.\nThe sum of the numbers is {sum(arra)}")


#########################################################################################################################################
#############################################File Caller

def file_caller():
    fc_user_input = ""
    print("Checks if the file exists, if not creates one.")
    while fc_user_input != "quit":
        fc_user_input = input('>>Enter filename: ')
        try:
            with open(fc_user_input) as file:
                for a in file:
                    print(a)

        except:
            if fc_user_input.lower() == "quit":
                print("File caller is leaving..")
                break
            else:
                print("No such file! Do you want me to create one in that name?\n Press 'y' to agree.")
                fc_2_input = input('>>')
                if fc_2_input.lower() == "y":
                    with open(fc_user_input, "wb") as file:
                        print(f"{fc_user_input} is created!")
                        pass


####################################################################################################################################
def prime_limit():
    from colorama import Fore, Style
    green = Style.BRIGHT + Fore.GREEN
    blue = Style.BRIGHT + Fore.BLUE
    red = Style.BRIGHT + Fore.RED
    reset = Style.RESET_ALL
    print(green + "This function calculates all the prime numbers in range the limit is given.\nType 'quit' to quit")
    while True:
        y = input(f"{reset}Give a limit: ")
        try:
            y = int(y)
            prime_store = []
            not_prime = []
            for i in range(1, y + 1):
                r = list(filter(lambda x: i % x == 0, range(1, y + 1)))
                if len(r) != 2:
                    not_prime.append(i)
                else:
                    prime_store.append(i)
            print(f"Prime numbers: {prime_store}")
            count = 0
            for a in prime_store:
                count += a
            print(f"        Sum of all " f"{blue}prime numbers is>>> {count}")
            print(f"{reset}Non-prime numbers: {not_prime}")
            not_count = 0
            for a in not_prime:
                not_count += a
            print(f"        Sum of all " f"{red}non-prime numbers is>>> {not_count}")
        except:
            if y == "quit":
                print(blue + "See you sir")
                break
            print(red + "Only numbers are allowed.")
            continue


###################################################################################
##################################### Taşk kağıt makas
def rock_paper_scissor():
    from random import choice

    moves = ["rock", "paper", "scissor"]
    out_of_chances, score_com, score_user, computer_won = 0, 0, 0, False
    print("Welcome. Print rock, paper, or scissor to take an action!")
    while True:
        try:
            play_rounds = int(input("How many rounds do you want to play: "))
            break
        except:
            print("Please enter a number.")
            continue
    while out_of_chances < play_rounds:
        computer_won, draw = False, False
        guess = input(">Take an action!: ").lower()
        computer = choice(moves)
        if guess not in moves:
            print("Take a proper action; rock, paper, scissor")
            continue
        if computer == guess:
            out_of_chances += 1
            print("Draw round!")
            draw = True
        elif ((computer == "rock" and guess == "scissor") or
              (computer == "paper" and guess == "rock") or
              (computer == "scissor" and guess == "paper")):
            print(f"{computer} vs {guess}. Computer wins!")
            score_com += 1
            computer_won = True
            out_of_chances += 1
        else:
            print(f"{computer} vs {guess}. User wins!")
            score_user += 1
        if not computer_won and not draw:
            out_of_chances += 1
        print(
            f"###########################Round {out_of_chances} is over! {str(play_rounds - out_of_chances)} left. #############################################")
    if score_user < score_com:
        print(f"    Computer won {score_com} out of {play_rounds} rounds.")
    elif score_com < score_user:
        print(f"    User won {score_user} out of {play_rounds} rounds.")
    elif score_user == score_com:
        print("     Draw game!")

############################Keygen###########################################################
def keygen():
    import random

    key_array = []
    keys = "MKXTI9BERLWC1D7ZGP032AOF8NHYU4S6VQ5J"
    box1, box2, box3,box4,box5 = "", "", "","",""
    for a in keys:
        key_array.append(a)
    x=2
    while len(box1)!=5:
        letter = random.choice(key_array)
        box1+=letter
    new_array =[]
    while len(box2)!=5:
        letter = random.choice(key_array)
        box2+=letter
    while len(box3)!=5:
        letter = random.choice(key_array)
        box3+=letter

    while len(box4)!=5:
        letter = random.choice(key_array)
        box4+=letter
    while len(box5)!=5:
        letter = random.choice(key_array)
        box5+=letter

    new_array.extend([box1,box2,box3,box4,box5])
    print(*new_array,sep="-")
######################################################################################33
def random_math():
    from random import randint, choice
    import operator

    mem,count,round_count = "0123456789-.",0,1
    operators = {"+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul}
    array_operator = ["+", "-", "/"]
    print("Bölme işleminde sadece ilk iki haneyi yazmalısın. Örn: 4.24\n 'q' çıkış")
    while True:
        luck = randint(0, 3)
        if luck == 0 or luck == 1 or luck == 2:
            a, b = randint(0, 1000), randint(0, 1000)
            get_islem = choice(array_operator)
            islem = operators.get(get_islem)
        else:
            a, b = randint(0, 100), randint(0, 100)
            get_islem = "*"
            islem = operators.get(get_islem)
        result = islem(a, b)
        print(f"\t\t-------Raund {round_count}-------")
        print(a, get_islem, b, "=", result)## Her şey tamamlanınca resultı kaldır.
        try:
            while True:
                is_valid = True
                guess = input("Sonuç = ")
                if guess == "q":
                    print(f"{round_count-1} sorudan {count} tanesini doğru bildin.\nEscaping...")
                    quit()
                round_count += 1
                for a in guess:
                    if a not in mem:
                        is_valid = False
                        print("Sadece sayı kullanabilirsin!")
                        break
                if not is_valid:
                    continue
                else:
                    if get_islem == "/":
                        result = str(result)
                        result = result[:4]
                    else:
                        guess = int(guess)
                    if guess == result:
                        print("Tebrikler!")
                        count+=1
                        break
                    else:
                        print("Hayır. Sonuç =", result)
                        break
        except Exception as e:
            print(e)
            continue

#####################################################matrix##########################################
def matrix():
    import random as r
    import time
    from colorama import Fore,Style

    green = Style.BRIGHT+Fore.GREEN
    print(green+"")
    symbols = ["0", "1", " ", " "]
    line = []
    counter = 0
    r_symbols = []
    for i in range(118):
        x = r.randint(0, 3)
        line.append(symbols[x])
        counter += 1

    for i in range(10000):
        if counter %5 ==0:
            r_symbols = [r.randint(0,117) for x in range(10)]
        for i in r_symbols:
            line[i]= symbols[r.randint(0,3)]

        print(*line)
        counter+=1
        time.sleep(0.01)

###################################################################################################
def mail_validator():
    import re
    print("This function takes user's e-mail adress and saves it as a global variable named 'email'")
    pattern = r"([\w\.-]+)@([\w\.]+)([\.\w]+)"
    while True:
        stra = input("Enter your mail adress: ")
        try:
            global email
            email = re.search(pattern, stra)
            print(email.group())
            email = email.group()
            break
        except:
            print("Please enter a valid e-mail!")
            continue
######################################################################################################
def letter_combination():
    print("This function takes your letter inputs and gives you their combination.\n 'quit' to break letters")
    from itertools import permutations,product
    letter_list = []
    while True:
        enter_letters= input("Enter the letters. One letter every time: ")
        if enter_letters=="quit":
            break
        if enter_letters not in letter_list:
            letter_list.append(enter_letters)
        else:
            print(f"The letter '{enter_letters}' already exists!")

    a = permutations(letter_list)
    len_permute = 0
    for b in a:
        print(*b,sep= "-")
        len_permute+=1
    print(len_permute,"Elements")
##############################################################################################################
def number_generator():
    from time import sleep
    from random import randint
    print("This function takes a number and generates a sequence of numbers in it's range.")
    while True:
        try:
            user_number = int(input("Enter your number range: "))
            user_times = int(input("How many numbers you  want: "))
            print(f"Creating sequence of numbers in range '{user_number}'")
            break
        except:
            print("Enter a number please!")
            continue
    checklist,randlist,previous,counter,my_dic = [],[], None,0,{}
    for a in range(user_number+1):
        checklist.append(a)
    for b in range(user_times+1):
        num = randint(0,user_number+1)
        randlist.append(num)

    print(*randlist)
    print("Correcting number orders..")
    randlist.sort()
    print(*randlist)
    for c in checklist:
        if c==previous:
            continue
        if c in randlist:
            counter = randlist.count(c)
            my_dic[c] = "exists "+str(counter)+" times"
        else:
            my_dic[c] = "doesn't exist..."
            previous,counter =c,0

    for key,value in my_dic.items():
        print(key,value)
    print("\t\tFull numbers:")
    print(*randlist)
    print("\t\tEven numbers:")
    print(list(filter(lambda x:x%2==0,randlist)))
    print("\t\tOdd numbers: ")
    print(list(filter(lambda x:x%2==1,randlist)))
#################################################################################################################################################3






def turkish_character():
    turkish = "abcçdefgğhıijklmnoöprsştuüvyz "
    print("Verdiğin cümle, Türkçedeki bütün karakterleri içeriyor mu diye test eder.")
    while True:
        missing_list = []
        sentence = input("Cümleyi gir: ").lower()
        if sentence =="q" or sentence =="quit":
            break
        for a in turkish:
            if a not in sentence:
                missing_list.append(a)
        if len(missing_list)==0:
            print("Bu cümle bütün Türkçe karakterleri içeriyor.")
        else:
            print(f"Cümlende eksik {len(missing_list)} harf var: ",*missing_list,sep=",")

#########################################################################################################################

#################################################################################################################################################
def statistics():
    clear()
    from colorama import Fore,Style,init
    from scipy import stats
    import numpy

    init()
    red = Style.BRIGHT+Fore.RED
    yellow = Style.BRIGHT+Fore.YELLOW
    default = Style.RESET_ALL

    while True:
        numbers = []
        is_okay = True
        number_input = input('Enter the numbers splitting with comma.Example:1,2,3,4\nNumbers: ').split(',')
        if 'q' in number_input:
            print('Leaving..')
            break
        for a in number_input:
            if a.isdigit():
                a = int(a)
                numbers.append(a)
            else:
                print("Incorrect input '{0}'.".format(a))
                is_okay = False
            continue
        if is_okay:

            print('Numbers entered:',*numbers)
            numbers = sorted(numbers)
            print(len(numbers),'elements.Sorted:',*numbers)
            x = numpy.mean(numbers)
            print(red,'Mean:',yellow,x)
            x= numpy.median(numbers)
            print(red,'Median:',yellow, x)
            x = stats.mode(numbers)
            print(red,'Mode:',yellow, x)
            x = numpy.std(numbers)
            print(red,'Standard Deriation:',yellow, x)
            x = numpy.var(numbers)
            print(red,'Variation is:',yellow, x,default)



###################################################################


def neo(name='Neo'):
    from colorama import Fore,Style
    import os
    import sys
    import time
    print(Style.BRIGHT+Fore.GREEN)
    clear()
    while True:
        text = '....'
        text2= f'Wake up {name.title()}.....'
        text3 = f'Follow the white rabbit {name.title()}!'
        for letter in text:
            print(letter,end = '')
            sys.stdout.flush()
            time.sleep(0.24)
        clear()
        for letter in text2:
            print(letter, end='')
            sys.stdout.flush()
            time.sleep(0.24)
        clear()
        for letter in text3:
            print(letter, end='')
            sys.stdout.flush()
            time.sleep(0.14)
        a = input()
        if a=='q':
            break
        elif a=='follow':
            return matrix()
#############################################################################################3
def tc_ilkdokuz():
    while True:
        try:
            tc = int(input('>'))
        except:
            print('T.C. no sayı olmak zorundadır!')
            qqq = input('Çıkmak için q yaz')
            if qqq=='q':
                break
            else:
                continue
        stringtc = str(tc)
        tekler = [stringtc[0],stringtc[2],stringtc[4],stringtc[6],stringtc[8]]
        ciftler = [stringtc[1],stringtc[3],stringtc[5],stringtc[7]]
        tektoplam =0
        cifttoplam = 0
        for a in tekler:
            a= int(a)
            tektoplam+=a
        for b in ciftler:
            b = int(b)
            cifttoplam+=b
        print(tektoplam)
        print(cifttoplam)
        on_hane = (tektoplam*7-cifttoplam)%10
        onbir_hane = (tektoplam+cifttoplam+on_hane)%10
        stringtc+=str(on_hane)
        stringtc+=str(onbir_hane)
        print(stringtc)
        break

##########################################################3#####
def tc_validate():
    while True:
        tc = input('TC No> ')
        if len(tc)!=11:
            if tc=="q":
                break
            else:
                print("11 hane olmak zorundadır!\nÇıkış için 'q' yazınız. ")
                continue
      
        teklerToplam=0
        ciftlerToplam=0

        for a in range(0,9,2):
            teklerToplam+= int(tc[a])
        for b in range(1,8,2):
            ciftlerToplam+= int(tc[b])

        on_hane = (teklerToplam*7-ciftlerToplam)%10
        onbir_hane = (teklerToplam+ciftlerToplam+on_hane)%10

        #10 ve 11. haneleri karşılaştır.
        tcHaneOn = int(tc[9])
        tcHaneOnBir = int(tc[10])
        if tcHaneOn==on_hane and tcHaneOnBir==onbir_hane:
             print('Tc kimlik no doğru.')
        else:
            print('TC no geçerli değil!')

#####################################################################
def summations_calculator():
    print('This function prints the given operations in a specific range.\nType q to quit.')
    import operator
    import re

    total = 0
    operation_dic = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv,
                     '//': operator.truediv, '**': operator.pow,'%':operator.mod}
    while True:
        get_numbers = input('Valid format: 2 4 *2\n>>>')
        if get_numbers == 'q':
            break
        pattern = r"[0-9] [0-9]([0-9])* [+-/*%][+-/*]*[0-9]"  # checks the pattern

        if not re.search(pattern, get_numbers):
            print('Invalid format!')
            continue

        try:
            first, second, third = get_numbers.split()
            first = int(first)
            second = int(second)
            expression = third[0]  # find the expression.
            expression_str = ''
            if third.count(expression)>1: # for // and **
                expression_str +=third[0]+third[0]

            third = third.replace(expression, '')  # remove the expression to convert it to an integer.
            expression = operation_dic.get(expression_str)
            third = int(third)
        except Exception as f:
            print(f)
            break
        for a in range(first, second + 1):
            result = expression(a, third)
            total += result
            print(a, expression_str, third, '=', result)
        print(f'Sum of the results: {total}')
        total = 0


#####################################################################

def agent_number_code():
    x = random.randint(1,30)
    y = random.randint(1,30)
    z = random.randint(1,30)
    
    sum = x+y+z
    pro = x*y*z


    user_sum  = 0
    user_pro = 0
    while user_sum!=sum and user_pro!=pro:
        print(f"\n\n\nSum of my numbers is: {sum}")
        print(f"Multiplication of my numbers is: {pro}")

        try:
            num1,num2,num3 = input('Enter your numbers with a space: ').split()
            num1 = int(num1)
            num2 = int(num2)
            num3 = int(num3)
            user_sum  = num1+num2+num3
            user_pro = num1*num2*num3
        except Exception as f:
            print(f)
            if num1=='q':
                exit()
    else:
        print('great')


#####################################################################
def calculate_money_currency():
    import requests
    import json

    while True:
        available_money_types = []
        
        result = requests.get(f"https://api.exchangeratesapi.io/latest?base=USD")

        result  = json.loads(result.text)
        for a in result["rates"]:
            available_money_types.append(a)

        print("Available money types: ",*available_money_types,sep=", ")

        try:
            money_type = input("Base money: ").upper()
            target_currency = input("Target money: ").upper()
            money_amount = int(input(f"How many {money_type}: "))
        except Exception as wtf:
            print(wtf)
            continue

        result = requests.get(f"https://api.exchangeratesapi.io/latest?base={money_type}")

        result  = json.loads(result.text)

        value = result["rates"][target_currency] #döviz değeri

        print(f"\n\n1 {money_type} = {value} {target_currency}")
        print(f"{money_amount} {money_type} = {value*money_amount} {target_currency}")
        wants_to_do_again = input("Type 'y' to calculate again.").lower()
        if wants_to_do_again=='y':
            continue
        else:
            break





#####################################################################
import os
clear = lambda: os.system('cls')
my_guide()
while True:

    action = input("(admin)>>>>Enter the action: ")
    if action =="info":
    	my_guide()
    	continue
    elif action=="cls":
    	clear()
    	continue
    
    try:
    	eval(action)
    except Exception as e:
    	print(e)