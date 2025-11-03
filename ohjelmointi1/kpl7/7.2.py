nimi = str(input("Anna nimi"))
nimet = {"Jaakko", "Liisa"}

while nimi != "":

    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")

    nimet.add(nimi)
    nimi = str(input("Anna nimi"))

for i in nimet:
    print(i)
