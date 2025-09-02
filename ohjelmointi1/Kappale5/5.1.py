nopat = []
loop = 0
import random
n = int(input("Anna noppien luku määrä"))

while n > loop:
    noppa = random.randint(1,6)
    nopat.append(noppa)

    loop = loop + 1

summa = 0
for i in nopat:
    summa = summa + i
    print(nopat)


print(summa)



