import requests
import json

api_key='2b4baac3760a68f01d98e5f6a5e8825f'

city = input("Anna kaupungin nimi: ")

url= "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric&lang=fi"


try:
    response = requests.get(url)
    #print(r)

    if response.status_code == 200:
        data = response.json()
        #print(json.dumps(data, indent=2, ensure_ascii=False))

        temperture = data['main']['temp']
        weather = data['weather'][0]['description']
        name = data['name']

        print("\n" f"Säätiedot {name}: ")
        print(f'Lämpötila: {temperture}C°')
        print(f'Sää: {weather}')
except Exception as e:
    print(e)


