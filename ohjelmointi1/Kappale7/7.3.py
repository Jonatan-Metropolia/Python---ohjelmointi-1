valinta = 0
lentoasemat = {}

def lisää():

    icao = str(input("Anna ICAO-koodi"))
    asema = str(input("Anna lento asema"))
    lentoasemat[icao] = asema
    return lentoasemat

def tiedustelu():
    icao = str(input("Anna ICAO-koodi"))
    if icao in lentoasemat:
        print(f'Antamaasia ICAO-koodia vastaavan lento aseman nimi on "{lentoasemat[icao]}"')
    else:
        print("Antamasi ICAO-koodi on väärä tai ei löydy tietokannasta")


while valinta != 3:
    valinta = int(input("Valitse seuraavista:"
                    "\n1. Etsi mitä lento asemaa ICAO-koodisi vastaa"
                    "\n2. Lisää uusi lento-asema tietokantaan"
                    "\n3. Lopeta ohjelma"
                    "\n->"))
    if valinta == 1:
        tiedustelu()
    elif valinta == 2:
        lisää()



