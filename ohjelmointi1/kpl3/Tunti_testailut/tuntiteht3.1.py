#kysytään ikää
ikä = int(input("Anna ikäsi"))

#Tarkistetaan onko täysi ikäinen vai ei
if ikä >= 18:
    print("Voit äänestää!")
else:
    #lasketaan paljonko ikää puuttuu
    vajaus = 18-ikä
    print(f"Et voi äänestää, voit äänestää {vajaus} kuluttua.")
#