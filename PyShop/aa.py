import sqlite3
connection = sqlite3.connect('db.sqlite3') #veritabanıma bağlanıyorum.

cursor = connection.execute("")

for a in cursor:
	print(a)