import mysql.connector
import geopy
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

cordinates=[]
#setup
yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="JonatanGM",
    password="123",
    database="flight_game",
    autocommit=True,
)

def icao_to_gps(icao):
    sql = f"select gps_code from airport where ident='{icao}'"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos['gps_code']

for i in range(2):
    icao = input("Anna ICAO koodi")
    gps = icao_to_gps(icao)

    geolocator = Nominatim(user_agent="kpl8")
    location = geolocator.geocode(gps)

    cordinates_list= (location.latitude, location.longitude)
    cordinates.append(cordinates_list)

distance = geodesic(cordinates[0], cordinates[1]).km
print(distance)


'''
Jokin bugi tulee välillä. liittyy kaiketi verkko palvelimeen josta sijainti haetaan.
'''




