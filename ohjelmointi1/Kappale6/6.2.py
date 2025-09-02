import random

def ran (tahkot):
    return random.randint(1,tahkot)

tahko = int(input("Anna nopan tahkojen määrä"))

noppa = ran(tahko)
heitot = 1

while noppa != tahko:
    print(noppa)
    noppa = ran(tahko)
    heitot = heitot+1

print(f"{noppa}\n Suurimman silmäluvun saaminen kesti {heitot} heittoa")
