import requests
import json


headers = {
    "Accept": "application/json",
    "User-Agent": "playing with APIs in python and github actions, I'm here over at github.com/msoup"
}

def displayRandomJoke():
    response = requests.get("https://icanhazdadjoke.com/", headers=headers)
    print(response.json())