hunger = 5
happiness = 5
sleep = 5
import random
def randomi(happiness):
    random_value = random.uniform(1, 1/happiness)
    random_value = max(0, random_value)
    return random_value

def sleep_hunger(sleep_value, hunger_value):
    if sleep_value > 5:
        sleep_value = sleep_value-5
        hunger_value = hunger_value+2
    else:
        hunger_value += sleep_value/2.5
        sleep_value = 0
    return sleep_value, hunger_value

loop = True
print("Hoida possua ja pidä huoli ettei se nälkäänny\n"
      "Voit valita mitä teet joka kierroksella painamalla:\n"
      "Paina aluksi mitä tahansa näppäintä jatkaaksesi peliin\n"
      "'1', Syötä possua\n"
      "'2', Leiki possun kanssa\n"
      "'3', Pistä possu nukkumaan\n"
      "'4', Älä tee mitään")

choise = input("")

while loop == True:
    print(f"Possun nälkä on {hunger} (Possu kuolee kun nälkä on 10)  ------- Syötä = '1'\n"
          f"Possun iloisuus on {happiness} (Voitat pelin saavutettuasi 10) - Leiki = '2'\n"
          f"Possun väsymys on {sleep} (Possu vaipuu koomaan jos 10)  ------- Nuku  = '3'")
    choise = input("")
    if choise == "1":
        hunger = max(0, hunger-1)
        sleep += 1
    elif choise == "2":
        happiness += randomi(happiness)
        sleep += 1
        hunger += 1
    elif choise == "3":
        new_sleep, new_hunger = sleep_hunger(sleep, hunger)
        hunger = max(0,new_hunger)
        sleep = max(0,new_sleep)
    elif choise == "4":
        sleep += 1
        hunger += 1
        happiness -= 1
    else:
        print("Painoit väärä näppäintä")




    if hunger >= 10:
        loop = False
        print("Hävisit pelin\n"
              "Possu kuoli nälkään :(")
    elif sleep >= 10:
        loop = False
        print("Hävisit pelin\n"
              "Possu vaipui koomaan :(")
    elif happiness >= 10 > sleep and hunger < 10:
        loop = False
        print("voitit pelin")
    elif happiness <=0:
        loop = False
        print("Hävisit pelin\n"
        "Possu masentui :(")



