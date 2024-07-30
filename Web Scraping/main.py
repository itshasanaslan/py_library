from bs4 import BeautifulSoup

html_doc  = """
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>My First Page</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
  
</head>
<body>
    
    <h1 id="header">
        Python Course
    </h1>

    <div class="group1">
    <h2>Programming</h2>
    <ul>
        <li>Menu 1</li>
        <li>Menu 2</li>   
        <li>Menu 3</li>
    </ul>
    </div>
    <div class="group2">
        <h2>Modules </h2>
        <ul>
        <li>Menu 1</li>
        <li>Menu 2</li>   
        <li>Menu 3</li>
    </ul>
    </div>

</body>
</html>

"""

soup = BeautifulSoup(html_doc,"html.parser")
result = soup.prettify()
result = soup.h2.text # soup.h2.text yada soup.h2.name de olabilir.
result = soup.find_all('h2') # bütün h2 leri bulur.
result = soup.find_all('h2')[0] # bunu anlarsin zaten.
result = soup.div.findChildren() # div altındaki her şeyi alır.
result = soup.div.findNextSibling().findNextSibling()
result  = soup.findAll('a') # a href linklerine erişim
for link in result:
    print(link.get('href'))

print(result)


#####################################################################################
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
