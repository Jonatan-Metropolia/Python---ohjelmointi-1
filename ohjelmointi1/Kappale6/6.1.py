import random

def randomi ():
    return random.randint(1,6)

def main():
    dice = 0
    while dice != 6:
        dice = randomi()
        print(dice)


main()



