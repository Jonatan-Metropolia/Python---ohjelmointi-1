import mysql.connector

yhtes = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="JonatanGM",
    password="123",
    database="flight_game",
    autocommit=True,
)

small_airport = 0
heliport = 0
medium_airport = 0
large_airport = 0

def airport_num (code):
    sql = f"select airport.type from airport where iso_country='{code}'"
    airport = yhtes.cursor(dictionary=True)
    airport.execute(sql)
    tulos = airport.fetchall()

    return tulos


code = input("Country code: ")
type = airport_num(code)
for i in type:
    if i['type'] == "small_airport":
        small_airport += 1
    elif i['type'] == "heliport":
        heliport += 1
    elif i['type'] == "medium_airport":
        medium_airport += 1
    elif i['type'] == "large_airport":
        large_airport += 1



print(f"Small airport = {small_airport}\n"
      f"Heliport = {heliport}\n"
      f"Medium airport = {medium_airport}\n"
      f"Large airport = {large_airport}")

