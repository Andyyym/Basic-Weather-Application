from urllib import response
from weakref import WeakSet
import requests

API_KEY = "ADD_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a ciy name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    tempreature = round(data["main"]["temp"] - 273.15, 2)

    print("Weather:", weather)
    print("Temperature:", tempreature, "celsius")

else:
    print("An Error Occured")