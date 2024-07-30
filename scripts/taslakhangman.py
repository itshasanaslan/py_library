word = "hasan"
blank =[]
for a in word:
    blank.append("_")
print(blank)
while True:
    guess=input(">>")
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                blank[i]=guess
        print(*blank)