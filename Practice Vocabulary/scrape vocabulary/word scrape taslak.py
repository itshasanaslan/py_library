import requests
from bs4 import BeautifulSoup

url = "https://www.macmillandictionary.com/dictionary/british/declare" #bu kelimeyi düzenle
html  = requests.get(url).content
soup = BeautifulSoup(html,'html.parser')
soup.prettify()

#my_soup = soup.find('div',{"class":"THES"}).find("a")
my_soup = soup.find('a',{"class":"h2"}).contents[0]



print(my_soup)