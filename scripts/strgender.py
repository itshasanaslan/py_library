## Bu da bool kullanmadan yapılan alternatif versiyonu. Ama kontrol açısından bool daha iyi.
a = 0
gender = "a"
age = "b"
height = "c"
is_male = input("Are you a male or a female?\n")
while True:
    try:
        is_tall = int(input("What's your height? Centimeters without dot; 175\n"))
        age = int(input("What is your age?\n"))
        break
    except:
        print("Enter a number!!")
if is_male.lower() == "male":
    gender = "male"
elif is_male.lower() == "female":
    gender = " female "
else:
    a = 2
    print("GENDER INPUT CAUSES THIS ERROR")
while a == 2:
    print("GENDER INPUT CAUSES THIS ERROR")

if is_tall >= 175:
    height = " tall "
else:
    height = " short"
if age > 0:
    age = " young "
elif age >= 30 and (age < 45):
    age = " a middle-aged "

elif age >= 45:
    age = "an old"
else:
    print("age error")
print("You are " + str(age) + gender + " and you are " + height)