import os
os.system('title ASLAN package manager')
exception_list = []
install_packages = ['numpy','-U discord.py[voice]','-U youtube_dl','pygame',
'colorama','pynput','openpyxl','matplotlib','scipy','bs4','lxml',
'https://github.com/pyinstaller/pyinstaller/archive/develop.zip','pywin32','discord','discord.py',"requests","selenium","youtube-dl","youtube-dl --upgrade"]
while True:
	print(install_packages)
	add_packages = input('Enter the packages you want to install with a space: ').split()
	install_packages.extend(add_packages)
	break
for a in install_packages:
	try:
		os.system(f'pip install {a}')
	except Exception as f:
		exception_list.append(f)

print('\n'*6)
if len(exception_list)==0:
	print('All modules installed successfully.')
else:
	print("Caught Exceptions: ")
	for a in exception_list:
		print(a)

input()