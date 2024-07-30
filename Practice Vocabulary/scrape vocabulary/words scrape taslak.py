import requests
from bs4 import BeautifulSoup

url = "https://www.macmillandictionary.com/dictionary/british/"

words= ["declare","assign","mock","love",'anchor','misery','happiness']

for word in words:	
	html  = requests.get(url+word).content
	soup = BeautifulSoup(html,'html.parser')
	soup.prettify()
	#my_soup = soup.find('div',{"class":"THES"}).find("a")
	my_soup = soup.find('a',{"class":"h2"}).contents[0]
	part_of_speech = soup.find('span',{"class":"PART-OF-SPEECH"}).contents[1]
	print(f"{part_of_speech}) {word} : {my_soup}")