kuha = float(input("Kuinka pitkä kuha on?"))
if kuha < 37:
    print("Kuha on liaan pieni. Laske se heti takaisin!")
    kuhanpuuttuva = 37-float(kuha)
    print("Kuhan pituudesta puuttuu " + str(kuhanpuuttuva) + "cm")
else:
    print("Kuha on tarpeeksi iso, voit pitää sen!")
