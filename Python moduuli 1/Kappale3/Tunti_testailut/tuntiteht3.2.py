kulutus = float(input("Anna kWh kulutuksesi"))
if kulutus <0:
    print("negatiivista kulutusta ei voi laskea")
    hinta = 0.0
elif kulutus <= 50:
    hinta = kulutus * 0.1
elif kulutus <= 200:
    hintaA = 50*0.1
    yli50 = kulutus-50
    hintaB = yli50*0.08
    hinta = hintaA+hintaB
else:
    hintaA = 50*0.1
    hintaB = 150*0.08
    yli200 = kulutus-200
    hintaC = yli200*0.06
    hinta = hitaA+hintaB+hintaC
print(f"sähkön kulutuksesi on {hinta} €")
#