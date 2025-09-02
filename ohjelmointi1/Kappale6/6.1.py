import random

def randomi ():
    return random.randint(1,6)


noppa = randomi()

while noppa !=6:
    print(noppa)
    noppa = randomi()

print(noppa)

