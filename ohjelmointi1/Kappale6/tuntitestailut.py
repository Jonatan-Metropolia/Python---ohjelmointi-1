import random

def randomi (loppu):
    return random.randint(1,loppu)


y= int(input("anna loppu luku"))


noppa = randomi(y)

while noppa !=1:
    print(noppa)
    noppa = randomi(y)

print(noppa)

