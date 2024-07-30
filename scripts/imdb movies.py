#https://www.imdb.com/chart/top/?ref_=nv_mv_250 buraya gidip sag tiklayip sayfa kaynagini goruntuledim ve html kodlarına ulastim.

from bs4 import BeautifulSoup
import requests
import json

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

'''
response = requests.get(url)
print(response) sonucun basarili bir şekilde gelip gelmedigini test et.
'''
html  = requests.get(url).content
soup = BeautifulSoup(html,'html.parser')

list = soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=10) #10 film yazdiracagim

id =1 
for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    id+=1
    print(f"{id}) Movie: {title.ljust(52)} | Year: {year} | Rating: {rating}")
