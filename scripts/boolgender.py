### Çalışıyor.
is_old,is_middle,is_young,is_tall,is_male,is_female = False,False,False,False,False,False,
is_male = input("Are you a male or a female?\n")
while True:
    try:
        is_tall = int(input("What's your height? Centimeters without dot; 175\n"))
        age = int(input("What is your age?\n"))
        break
    except:
        print("You need to enter numbers, not a characters!")
if is_male.lower() == "male":
    is_male = True
elif is_male.lower() == "female":
    is_female = True
    is_male = False
else:
    is_male = False
    is_female = False

if is_tall >= 175:
    is_tall = True
else:
    is_tall = False
if age > 0:
    is_old = True
if age >= 30 and (age < 45):
    is_middle = True
    is_old = False
elif age >= 45:
    is_old = True
else:
    is_young = True
    is_old = False
    is_middle = False
if not is_male and not is_female:
    print("Gender input error!")
elif is_male and is_young and is_tall:
    print("You are a young male and you are tall")
elif is_male and is_tall and is_middle:
    print("You are a middle-aged male and you are tall..")
elif is_male and is_tall and is_old:
    print("You are an old male and you are tall.")
elif is_male and not is_tall and is_young:
    print("You are a young male and you are short.")
elif is_male and not is_tall and is_middle:
    print("You are a middle-aged male and you are short.")
elif is_male and not is_tall and is_old:
    print("You are an old male and you are short")
elif is_female and is_young and is_tall:
    print("You are a young woman and you are tall")
elif is_female and is_tall and is_middle:
    print("You are a middle-aged woman and you are tall..")
elif is_female and is_tall and is_old:
    print("You are an old woman and you are tall.")
elif is_female and not is_tall and is_young:
    print("You are a young woman and you are short.")
elif is_female and not is_tall and is_middle:
    print("You are a middle-aged woman and you are short.")
elif is_female and not is_tall and is_old:
    print("You are an old woman and you are short")
else:
    print("Error. I couldn't figure out how you come here.")
