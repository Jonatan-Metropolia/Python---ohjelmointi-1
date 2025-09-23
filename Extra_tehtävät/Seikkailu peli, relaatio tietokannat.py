import mysql.connector


'''
Luodaan aluksi database MariDB:seen käyttäen pythonia, 
Tämö tarvitsee luoda vain kerran jonka jälkeen database on jo koneella.
MariaDB tarkistaa onko tietokantaa jo olemassa joten IF funktio ei tarpeen. 
Tämä ensimmäinen osio toimii vain ns luonti skriptinä
'''

yhteys_database_creation = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="140305",
    autocommit=True
)
# Määritetään cursor oikeaan tietokantaan
cursor = yhteys_database_creation.cursor()

# Debug varten poistetaan aina vanha
debug = input("Debug = 1, (reset)")
if debug == "1":
    cursor.execute("DROP DATABASE IF EXISTS seikkailu_peli;")




# Luodaan uusi tietokanta, IF NOT EXISTS estää luomasta kopiota ensikerran jälkeen.
cursor.execute("CREATE DATABASE IF NOT EXISTS seikkailu_peli;")

# annetaan oikeudet käyttäjälle JonatanGM
cursor.execute("GRANT ALL PRIVILEGES ON seikkailu_peli.* TO 'JonatanGM'@'localhost';")

# ladataan oikeudet
cursor.execute("FLUSH PRIVILEGES;")


#Luodaan seuraavaksi taulut/tables

#Otetaan seikkailu_peli tietokanta käyttöön
cursor.execute("USE seikkailu_peli;")
#pelaajan statsit
cursor.execute(
    "CREATE TABLE IF NOT EXISTS stats_player ("
    "player_id INT AUTO_INCREMENT PRIMARY KEY, "
    "health INT DEFAULT 20, "
    "damage INT DEFAULT 1, "
    "energy INT DEFAULT 100,"
    "weapon INT,"
    "name varchar(100)"
    ");"
)

# Vihollisten stats
cursor.execute(
    "CREATE TABLE IF NOT EXISTS stats_enemy ("
    "enemy_id INT AUTO_INCREMENT PRIMARY KEY, "
    "health INT DEFAULT 20, "
    "damage INT DEFAULT 1,"
    "name varchar(50)"
    ");"
)

# Mikä ase kyseessä
cursor.execute(
    "CREATE TABLE IF NOT EXISTS weapon_type ("
    "weapon_id INT AUTO_INCREMENT PRIMARY KEY, "
    "weapon_name varchar(50) NOT NULL, "
    "weapon_damage INT NOT NULL"
    ");"
)

# Lisätään seuraavaksi tauluihin sisältö

#   %s = tuple    ||   (%s, %s) = (muuttuja_1, muuttuja_2)

#aloitetaan aseista:
cursor.execute("INSERT INTO weapon_type (weapon_name, weapon_damage) VALUES (%s, %s)",
               ("Diamond Sword", 7))
cursor.execute("INSERT INTO weapon_type (weapon_name, weapon_damage) VALUES (%s, %s)",
               ("Iron Sword", 4))
cursor.execute("INSERT INTO weapon_type (weapon_name, weapon_damage) VALUES (%s, %s)",
               ("Stone Sword", 3))
cursor.execute("INSERT INTO weapon_type (weapon_name, weapon_damage) VALUES (%s, %s)",
               ("Hand", 1))

#lisätään viholliset:
cursor.execute("INSERT INTO stats_enemy (health, damage, name) VALUES (%s, %s, %s)",
               (20, 1, "zombie"))
cursor.execute("INSERT INTO stats_enemy (health, damage, name) VALUES (%s, %s, %s)",
               (20, 3, "skeleton"))
cursor.execute("INSERT INTO stats_enemy (health, damage, name) VALUES (%s, %s, %s)",
               (100, 10, "giant"))

yhteys_database_creation.close()


################################# MAIN!!!!! #################################
################################# MAIN!!!!! #################################
################################# MAIN!!!!! #################################

# Nyt yhdistetään sikkailu peliin
yhteys_seikkailu_peli = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="JonatanGM",
    password="123",
    autocommit=True
)
cursor = yhteys_seikkailu_peli.cursor()

cursor.execute("USE seikkailu_peli;")


# Määritellään vihollinen levelin mukaan
def vihollinen(level):
    if 1 <= level <= 4:
        enemy_name = "zombie"
    elif 5 <= level <= 8:
        enemy_name = "skeleton"
    elif level == 9:
        enemy_name = "giant"
    else:
        return None  # varmuuden vuoksi

    # haetaan aina vain yksi vihollinen "LIMIT" komennola
    cursor.execute("SELECT name FROM stats_enemy WHERE name = %s LIMIT 1", (enemy_name,))
    chosen_enemy = cursor.fetchone()
    return chosen_enemy[0] if chosen_enemy else None


def player_hp_check(player):
    cursor.execute("SELECT health FROM stats_player WHERE name = %s LIMIT 1", (player,))
    result = cursor.fetchone()
    return result[0] if result else None


loop = True
# Pelaajan valinta
while loop == True:
    save_game_check = input("Player Name: ")

    # Tarkistetaan onko pelaaja jo olemassa
    cursor.execute("SELECT name FROM stats_player WHERE name = %s LIMIT 1", (save_game_check,))
    row = cursor.fetchone()
    if row:
        print("Pelaaja nimi on varattu!")
        # Voidaan valita käyttää save gamea
        use_save_game = input("Haluatko käyttää kyseistä savegame? (y/n)")
        if use_save_game == "y":
            loop = False
            player = save_game_check

    else:
        cursor.execute("INSERT INTO stats_player (name) VALUES (%s)", (save_game_check,))
        player = save_game_check
        loop = False


print(f"Hei, {player}! Terve tuloa pelaamaan!\n"
      "Tehtäväsi on tappaa giant\n"
      "(painamalla 'ENTER' tyhjään ruutuun pääset keskusteluissa eteenpäin)")
# Käytetään input funktiota jotta käyttäjällä aikaa lukea tekstit eikä tule liikaa kerralla
input("")

input_check = True
game_loop = True
level = 1

while game_loop == True:
    current_enemy = vihollinen(level)
    print(f"{level}. vihollisesi on {current_enemy}\n"
          "Hyökkää/Karkaa (1/2)")

    while input_check == True:
        choise = input("")

        # hyökkäys
        if choise == "1":
            hp = player_hp_check(player)
            print(hp)
            input_check = False  # ettei jää loputtomaan looppiin

        # karkuu
        elif choise == "2":
            print("Pakenit taistelusta!")
            input_check = False

    input("")  # pysäytys ennen seuraavaa leveliä

    level = level + 1
    input_check = True  # nollataan seuraavaa kierrosta varten
