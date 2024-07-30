from random import randint


class Dice:
    def roll(self):
        first = randint(1, 6)
        second = randint(1, 6)
        return (first, second)


dice = Dice()
while True:
	input("Enter a key to roll a dice!")
	x,y = dice.roll()
	if x==y:
		print(f"Wow, same numbers: {x},{y}")
	else:
		print(f"{x},{y}")
		