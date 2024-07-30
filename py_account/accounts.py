import sqlite3
import datetime
import os
import crypto_helper
from prettytable import PrettyTable
import crypto_helper
import ctypes

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_KEY = os.path.join(BASE_DIR, "KEY.key")
db_path = os.path.join(BASE_DIR, "accounts.sql")

crypto_helper.load(MAIN_KEY)

def maximize_screen():
	kernel32 = ctypes.WinDLL('kernel32')
	user32 = ctypes.WinDLL('user32')
	SW_MAXIMIZE = 3
	hWnd = kernel32.GetConsoleWindow()
	user32.ShowWindow(hWnd, SW_MAXIMIZE)
	
maximize_screen()


class Account:
	def __init__(self, **kwargs):
		self.username = kwargs.get('username')
		self.password = kwargs.get('password')
		self.id = kwargs.get('id') if kwargs.get('id') else 0
		self.extra_notes = kwargs.get('extra')
		self.title = kwargs.get('title')
		if not kwargs.get('added_time'):
			self.added_time = str(datetime.datetime.now())
		else:
			self.added_time = kwargs.get('added_time')
	def __iter__(self):
		for attr, value in self.__dict__.items():
			yield attr, value

	def __str__(self):
		s = ""
		for i, j in self.__dict__.items():
			s += i.title() +" : " + str(j) + "\n" 

		s += ("-" * 20)
		return s

class Database:
	def __init__(self, **kwargs):
		self.connection = sqlite3.connect(kwargs.get('filename'))
		self.cryptography = kwargs.get("cryptography")

		print("Connected")


	def add(self, account):
		if type(account) != type(Account()):raise Exception("Please pass an account!")

		cursor = self.connection.cursor()
		data = self.converted_to_dict(account)
		if self.cryptography:
			data = self.hash(data)

		command = "Insert into Accounts (Title, Username, Password, ExtraNotes, AddedTime) Values (?,?,?,?,?)"
	#	cursor.execute(command, (data['title'], data['username'],  data['password'], data['extra_notes'], account.added_time))
		cursor.execute(command, (data.title, data.username,  data.password, data.extra_notes, account.added_time))

		self.connection.commit()		

	def get(self, account_id = -11):
		# if default id, return all
		cursor = self.connection.cursor()
		if account_id == -11:
			cursor.execute("Select * from Accounts")
			if self.cryptography:
				data = cursor.fetchall()
				decrypted = []
				for i in data:
					decrypted.append(self.unhash(self.parse(i, list = True)))
				return decrypted
			return cursor.fetchall()

		else: # return specific id
			command = "Select * from Accounts where Id = '?'"
			cursor.execute(command, (account_id))
			if self.cryptography:
				return self.unhash(cursor.fetchall())
			return cursor.fetchall()


	def update(self, account):
		cursor = self.connection.cursor()
		data = self.converted_to_dict(account)
		if self.cryptography:
			data = self.hash(data)

		command = "Update Accounts Set Title=:?, Username, Password, ExtraNotes, AddedTime) Values (?,?,?,?,?)"
	#	cursor.execute(command, (data['title'], data['username'],  data['password'], data['extra_notes'], account.added_time))
		cursor.execute(command, (data.title, data.username,  data.password, data.extra_notes, account.added_time))

		self.connection.commit()


	def remove(self, account_id):
		cursor = self.connection.cursor()
		command = f"Delete From Accounts where Id ='{account_id}'"
		cursor.execute(command)
		self.connection.commit()

	def first_creation(self, password):
		if password != "8448":
			raise Exception("What are you doing?")

		cursor = self.connection.cursor()
		cursor.execute("DROP TABLE IF EXISTS Accounts")

		#Creating table as per requirement
		sql ='''CREATE TABLE Accounts(
		Id integer not null primary key,
		   Title text,
		   Username text,
		   Password text,
		   ExtraNotes text,
		   AddedTime text)'''

		cursor.execute(sql)
		print("Created table!")

	def parse(self,data, **kwargs):
		if kwargs.get('list'):
			account = Account(
				username = data[2],
				password = data[3],
				title = data[1],
				extra = data[4],
				id = data[0],
				added_time = data[5])
		else:
			account = Account(
				username = data["username"],
				password = data["password"],
				title = data["title"],
				extra = data['extra_notes']
			)

		return account

	# Convert account to a dictionary
	def converted_to_dict(self, account):
		data = {}
		data['title'] = account.title
		data['username'] = account.username
		data['password'] = account.password
		data['extra_notes'] = account.extra_notes
		return data

	# Hash data
	def hash(self, data):
		d = {}
		for item, key in data.items():
			d[item] = self.cryptography.encrypt(key)
		return self.parse(d)
	
	#decrypt
	def unhash(self, data):
		data.title = self.cryptography.decrypt(data.title).decode()
		data.username = self.cryptography.decrypt(data.username).decode()
		data.password = self.cryptography.decrypt(data.password).decode()
		data.extra_notes = self.cryptography.decrypt(data.extra_notes)
		return data
		


a  = Account(
	username = "hasanaslan",
	password = "8448209aA",
	title = "test",
	extra_notes = "testing"
	)
db = Database(filename = db_path, cryptography = crypto_helper.crypto_manager)



def interface(database):
	global db
	def print_data():
		global db
		os.system('cls')
		print("-"*20)
		data = db.get()

		print(f"{len(data)} Accounts in records.")
		print('-'*20)
		
		table = PrettyTable()
		table.field_names = ['Id', 'Title', 'Username', 'Password', 'Extra Notes', 'Time']
		for acc in data:
			table.add_row([acc.id, acc.title, acc.username, acc.password, acc.extra_notes, str(acc.added_time)[0:16]])
			
		print(table)
		print("\n\n")

	while True:
		print_data()
		command = input("Enter a command: ")
		if command == 'refresh':
			print_data()
		elif command == 'add':
			d = {
			"username":None, "password":None, 'title':None, 'extra_notes': None
			}
			for item in d:
				d[item] = input(item + ": ")

			new_account = Account(
				username = d.get('username'),
				password = d.get('password'),
				title = d.get('title'),
				extra = d.get('extra_notes'))
			

			db.add(new_account)
			print_data()
			print("Added")

		elif command.split()[0] == "remove":
			if len(command.split()) < 2:
				input("Enter an Id!")
				continue
			db.remove(command.split()[1])
			input("Removed")
		elif command == 'q':quit()			
		else:
			print("Invalid command")
			continue	



interface(db)
