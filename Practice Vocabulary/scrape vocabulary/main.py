import requests
from bs4 import BeautifulSoup
import sqlite3

connection = sqlite3.connect("wordList.db")

cursor = connection.execute("select * from WordList")

words = []

for word in cursor:
	words.append(word[0])

index = len(words)


url = "https://www.macmillandictionary.com/dictionary/british/"



for word in words:
	try:
		html  = requests.get(url+word).content
		soup = BeautifulSoup(html,'html.parser')
		soup.prettify()
		#my_soup = soup.find('div',{"class":"THES"}).find("a")
		my_soup = soup.find('a',{"class":"h2"}).contents[0]
		part_of_speech = soup.find('span',{"class":"PART-OF-SPEECH"}).contents[1]
		print(f"({part_of_speech}) {word} : {my_soup}")
	except Exception as wtf:
		print(f"Skipped word: {word}::{wtf}")