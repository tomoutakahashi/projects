import openaq
import requests
import pandas as pd
from openaq import OpenAQ

key = 'd44ea67ee6c96be804e5e5660d99ae16d6f0c5dcb923828b8cfbabb649b6b33d'

def list_cities(country="US"):
    url = "https://api.openaq.org/v3/cities"
    params = {
        "country": country,
        "limit": 10
    }
    headers = {
        "x-api-key": key
    }

    r = requests.get(url, params=params,headers=headers)
    data = r.json()
    for city in data["results"]:
        print(city["city"])

list_cities()
