# Project#2: Weather App

import requests
import json
import win32com.client as wincom      # Importing API win32

city = input("Enter the name of city: ")

url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY={city}"

r = requests.get(url)
# print(r.text)
# print(type(r.text))    # <class 'str'>

weatherDictionary = json.loads(r.text)

w = weatherDictionary["current"]["temp_c"]
print(f"Current weather in {city}: ",w)  # Displaying current weather of city

speak = wincom.Dispatch("SAPI.SpVoice")

speak.Speak(f"The current weather in {city} is {w} degrees")  # Current weather in speech



