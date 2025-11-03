import time
import random
randomi = float(time.time())
kokonais = f"{(randomi):10.0f}"
desimaali = float(kokonais)-float(randomi)

kolme = round(abs(desimaali)*1000)
kolmetarkistus = float(kolme)
if kolmetarkistus < 100:
    print(kolme*10)
else:
    print(kolme)

luku1 = random.randint(1,6)
luku2= random.randint(1,6)
luku3 = random.randint(1,6)
luku4 = (random.randint(1,6))
neljä = str(luku1) + str(luku2) + str(luku3) + str(luku4)
print(int(neljä))

