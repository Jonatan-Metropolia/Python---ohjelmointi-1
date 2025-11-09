from flask import Flask
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


app = Flask(__name__)
@app.route('/airport/<airport>')
def airport(airport):

    sql = "SELECT name FROM airport WHERE ident = %s"

    cursor.execute(sql, (airport,))

    result = cursor.fetchone()

    vastaus = {
        "ICAO": airport,
        "Airport name": result
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)