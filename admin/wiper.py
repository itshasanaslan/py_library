import os
import getpass


def delete_all(path):
	for i in os.listdir(path):
		try:
			i  = os.path.join(path, i)
			with open(i , 'w') as file:
				file.write('wiped')
			os.remove(i)
			print("wiped ", i)
		except Exception as wtf:
			print(wtf)



def validate_pass():
	p = getpass.getpass(prompt='Password: ') 
	return p == "8448209aA"



os.system('title Aslan Wiper')
path = input("Enter path: ")



if path == "this":
	path = os.getcwd()

if not os.path.exists(path):
	print("Invalid path")
	exit()

accept = input("Warning, you are about to delete all of the content in this folder. Are u sure? y/n: ").lower()
if not accept in ["yes",'y']:
	quit()

if validate_pass():
	os.system('attrib -h -s')
	delete_all(path)
else:
	print("Invalid Password!")


input()