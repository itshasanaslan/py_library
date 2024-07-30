from pathlib import Path
import os
import os.path
import shutil



mem_dir = os.getcwd()
color = lambda: os.system('color f4')
clear = lambda:os.system('cls')
mypath=Path()
filename = ""

os.system('title r/hasanaslan')
try:
	print('Please wait.')
	os.system('pip search pyinstaller')
except:
	print('Installing module...')
	os.system('pip install pyinstaller')

setup_file = lambda:os.system(f'pyinstaller --onefile {filename}')
color()



def file_check():
	for file in mypath.glob("*.py"):
	 	print(f"\t{file}")
	
while True:
	os.chdir(mem_dir)
	clear()
	print('COMPATIBLE FILES ON YOUR DIRECTORY')
	file_check()
	print('\n\n')
	print('Using pyinstaller...')
	filename = input('Enter a filename: ')
	try:
		f = open(filename)
		path1 = filename[0:-3]
		isdir=os.path.isdir(path1)
		if not isdir:
			os.mkdir(path1)
		path =os.getcwd()
		file = path+f'\{filename}'
		target = path+f"\{path1}\{filename}"
		shutil.copyfile(file,target)
		path = path+f"\{path1}"
		os.chdir(path)
		setup_file()
		clear()
		os.system('color 0f')
		input(f'\n\n\nYour file is compiled. You can find it under the folder of \'{path1}\'.\nInside the \'dist\' folder, you can find your exe file.')
		input('Press enter to continue...')
		os.system('color f4')
	except:
		print('No such file.')
		input('...')


input()