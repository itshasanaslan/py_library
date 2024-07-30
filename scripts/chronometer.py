import time
import os

clear = lambda:os.system('cls')
os.system("title Aslan's stopwatch")

def regular():
	start = time.time()
	while True:
		clear()
		end = time.time()
		elapsed = round(end-start,2)
		print("Elapsed Time:",elapsed)

def counter_type(counter):
	input("Press any key to start.")
	while True:
		try:
			time.sleep(1)
			counter+=1
			clear()
			elapsed = counter//60
			secs = counter-(elapsed*60)
			print(f"Elapsed: {elapsed} minutes {secs} seconds ")
		except KeyboardInterrupt:
			input("Press any key to exit.")
			exit()


counter = 0

while True:

	choice = input("Type 1 for regular, Type 2 for counter method: ")
	#choice ='2'
	if choice=='1':
		regular()
	elif choice=='2':
		counter_type(counter)
	else:
		print("Wrong option")