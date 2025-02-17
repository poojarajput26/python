#1. weather : 

import requests
from bs4 import BeautifulSoup

def get_weather(city):
    url = f"https://www.weather-forecast.com/locations/{city}/forecasts/latest"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    weather = soup.find('span', class_='phrase').text
    print(f"Weather in {city}: {weather}")

city = input("Enter city: ")
get_weather(city)

