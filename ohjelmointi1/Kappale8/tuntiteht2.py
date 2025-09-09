import mysql.connector

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database = 'flight_game',
    user = 'JonatanGM',
    password = "123",
    autocommit = True,
)


def lentokenttahaku(koodi):
    sql = f"select * from airport where ident=%s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (koodi,))
    tulos = kursori.fetchall()
    print(tulos)
    return tulos

code = input('syötä koodi')
kentat = lentokenttahaku(code)

for i in kentat:
    print(i['name'])
