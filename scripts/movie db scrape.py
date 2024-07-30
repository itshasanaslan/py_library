import requests
import json
import os
#api = "684c1aa7617558af95ca334770dae429"


class MovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "684c1aa7617558af95ca334770dae429"

    def get_populars(self,page="1"):
        response = requests.get(self.api_url+"movie/popular?api_key="+self.api_key+"&language=en-US&page="+page)
        return response.json()

    def get_search_results(self,keyword,page="1"):
        response = requests.get(f"{self.api_url}search/keyword?api_key={self.api_key}&query={keyword}&page={page}")
        return response.json()


movieApi = MovieDb()
clear = lambda:os.system('cls')
os.system("title aslan movie scraper")

while True:
    choice  = input("1-)Popular Movies\n2-)Search Movies\n3-)Exit\n>>")
    
    if choice=="1":
        index = 1
        movies = movieApi.get_populars() # daha sonra page ayarlarını deneyebilirsin.
        for movie in movies['results']:
            print(f"{index}){movie['title']} Score:{movie['vote_average']}")
            index += 1

    elif choice=="2":
        index = 1
        keyword = input("Enter keyword: ")
        movies = movieApi.get_search_results(keyword)
        for movie in movies["results"]:
            print(f"{index}){movie['name']}")
            index += 1

    elif choice =="3":
        break
    wanna_clear = input("\n\n\ntype 'c' to clear.")
    if wanna_clear == "c":
        clear()