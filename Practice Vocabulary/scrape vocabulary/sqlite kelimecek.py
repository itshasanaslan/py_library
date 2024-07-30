import sqlite3

connection = sqlite3.connect("wordList.db")

cursor = connection.execute("select * from WordList")

for word in cursor:
	print(word[0]) #print(word)
