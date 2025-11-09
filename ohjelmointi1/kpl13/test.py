import mysql.connector

yhteys = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "140305",
    database = "flight_game",
    port = 3306,
    autocommit = True
)
cursor = yhteys.cursor()

airport = "EFAA"


sql = "SELECT name FROM airport WHERE ident = %s"

cursor.execute(sql, (airport,))

result = cursor.fetchone()