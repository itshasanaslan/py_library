mem = []
while True:
    filename = input("Enter a filename: ")
    try:
        with open(filename) as f:
            text = f.read()
        break
    except:
        print("No such file found!")


def checkletters(text):
    for d in text:  # önce metin içindeki karakterleri buluyorum.
        if d not in mem:
            mem.append(d)


def counter(text, char):
    count = 0
    for a in text:
        if a == char:
            count += 1
    return count


checkletters(text)
for char in mem:
    perc = 100 * counter(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))
print("There are {0} different characters in your text;".format(len(mem)))


def printer():
    for c in mem:
        print(c, end=" ")


while True:
    userin = input("Type \'see\' to see characters.Press any button to exit\n")
    if userin.lower() == "see":
        print(printer())
    else:
        print("Leaving...")
    break

"""
aa="abcdefghjklmnoprstuvyzqwx"
mem=["first"]
f=open("my_out","w+")
def func():
     c=1
     for letter in aa:
          f.write(f"{letter*c}\n")
          c+=1
     return c
func()
f.close()