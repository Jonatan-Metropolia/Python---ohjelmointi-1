import requests

r= 'https://api.chucknorris.io/jokes/random'

try:
    response = requests.get(r).json()
    print(response['value'])
except Exception as e:
    print(e)
