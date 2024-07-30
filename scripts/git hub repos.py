import requests
import json
import os

clear = lambda:os.system('cls')

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "43fea6fbadc383d54b0f28079e9a22c1732c626d"

    def get_user(self,username):
        response = requests.get(self.api_url + "/users/"+username)
        return response.json()

    def get_repositories(self,username):
        response = requests.get(self.api_url + "/users/"+username+"/repos")
        return response.json()


    def create_repositories(self,name):
        response = requests.post(self.api_url+"/user/repos?access_token="+self.token,json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
            })
        return response.json()



github = Github()
clear()

while True:
    choice = input("1-)Find user\n2-)Get Repositories\n3-)Create Repository\n4-)Exit\n>>")
    if choice=="1":
        print("Find User")
        username = input("Enter a username: ")
        result = github.get_user(username)
        #print(f"Name: {result['login']} public repos:{result['public_repos']} follower:{result['followers']}")
        for item in result:
            print(f"{item}: {result.get(item)}")

    elif choice=="2":
        print("Get Repositories")
        username = input("Enter a username: ")
        result = github.get_repositories(username)
        print("Repositories of",username,':')
        for repo in result:
            print(repo["name"])

    elif choice=="3":
        print("Create a Repository:")
        name = input("Enter a repository name: ")
        result  = github.create_repositories(name)
        print(result)

    elif choice=="4":
        break
    elif choice == "cls":
        clear()
        continue
    
    else:
        print("Invalid command!")
    print("\n********************************************************")