import sys
import os
import getpass
from colorama import Fore,init, Style

os.system('color 1f')
init()

class File:
	extension =  'aslan_enc'
	splitter = ',,'
	def __init__(self, location, directory_crawling = False):
		self.location = location
		self.fullname = ""
		self.name = ""
		self.output_name = ""
		self.extension = ""
		self.encrypted = False
		self.data = []
		self.parse_name('init')
		self.directory_crawling = directory_crawling
		

	def parse_name(self, *args):
		if args[0] not in ['init', 'encryption', 'decryption'] or len(args) < 1:
			raise Exception("Pass an argument to parse filename aslan.")

		if args[0] == 'init':
			n = ""

			for i in self.location:
				n += i

				if i in('\\','/'):
					n = ''

			fullname = n.split('.')
			self.fullname = n
			self.extension = fullname[-1]

			fullname.remove(self.extension)
			name = ""

			for i in fullname:
				name += i
			self.name = name

		elif args[0] == 'encryption':
			self.output_name = self.name + '.' +  self.extension + '.' + File.extension

		elif args[0] == 'decryption':
			d = self.fullname.split('.')
			d = d[0:-1] # omit File.extension

			for i in d:
				self.output_name += i + '.'
			self.output_name = self.output_name[0:-1] #omit last '.'
			


	def encrypt(self):
		with open(self.location, 'rb') as f:
			self.data = f.read()
		
		data = []
		for i in range(len(self.data)-1, -1, -1):
			data.append(self.data[i])
			
		self.encrypted = True
		self.parse_name('encryption')
		self.data = bytearray(data)

		
	def decrypt(self):
		if self.extension != File.extension and not self.directory_crawling:
			raise Exception(f"This file extension is not suitable with {File.extension}")
		with open(self.location, 'rb') as f:
			self.data = f.read()
		
		data = []
		for i in range(len(self.data)-1, -1, -1):
			data.append(self.data[i])
		
		self.data = bytearray(data)
		self.encrypted = False
		self.parse_name('decryption')

	def save(self):
		if self.encrypted:
			self.data = bytearray(self.data)
			with open(self.output_name,'wb') as f:
				f.write(self.data)
		# decrypted.			
		if not self.encrypted:
			with open(self.output_name, 'wb') as f:
					f.write(self.data)
		
		os.remove(self.location)




def pass_check():
	try: 
	    pw = getpass.getpass() 
	except Exception as error: 
	    print('ERROR', error)
	    sys.exit()
	else: 
	    if pw != '8448':
	    	print(Fore.RED+"Unauthorized!"+Fore.WHITE)
	    	sys.exit()
		



if len(sys.argv) != 3:
	raise Exception('Usage: python main.py filename e/d')
    	
if sys.argv[1] == 'alldir':
	files = os.listdir()
else:
	photo = File(sys.argv[1])

if sys.argv[2] == '-e':
	if sys.argv[1] == 'alldir':
		for i in files:
			if not i.endswith(File.extension):
				photo = File(i, directory_crawling=True)
				try:
					print(f"Now on {photo.fullname}: ",end='')
					photo.encrypt()
					photo.save()
					print("Encrypted as", photo.output_name)
				except Exception as f:
					print(f"{Fore.RED}Logged error for {i}: {f}{Style.RESET_ALL}")
		sys.exit()
	else:
		photo.encrypt()
		print("Encrypted as", photo.output_name)
elif sys.argv[2] == '-d':
	pass_check()
	if sys.argv[1] == 'alldir':
		for i in files:
			if i.endswith(File.extension):
				photo = File(i, directory_crawling=True)
				try:
					print(f"Now on {photo.fullname}: ",end='')
					photo.decrypt()
					photo.save()
					print("Decrypted as", photo.output_name)
				except Exception as f:
					print(f"Logged error for {i}: {f}")
		sys.exit()
	else:
		photo.decrypt()
		print('Decrypted as', photo.output_name)
else:
	raise Exception("Invalid parameter.")

photo.save()


# 0-255 ranginde ise sifrele.