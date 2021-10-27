import requests
import json


headers = {
    "Accept": "application/json",
    "User-Agent": "playing with APIs in python and github actions, I'm here over at github.com/msoup"
}

def getRandomJoke():
    response = requests.get("https://icanhazdadjoke.com/", headers=headers)
    return response.json()