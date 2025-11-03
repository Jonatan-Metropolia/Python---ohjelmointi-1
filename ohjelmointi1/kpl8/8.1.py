import mysql.connector

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database = 'flight_game',
    user = 'JonatanGM',
    password = "123",
    autocommit = True,
)

def haku(icao):
    sql = f"select municipality, name from airport where ident='{icao}'"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

icao = input("Anna ICAO-koodi")
tiedot = haku(icao)

for i in tiedot:
    print(i['name'], ",",  i['municipality'])