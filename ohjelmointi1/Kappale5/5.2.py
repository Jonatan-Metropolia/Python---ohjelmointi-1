loop = True
luvut = []

while loop == True:
    luku = input('Anna kokonais luku, paina "ENTER" tyhjään riviin')
    if luku != "":
        lukuint = int(luku)
        luvut.append(lukuint)
    else:
        loop = False

luvut.sort(reverse=True)
print(luvut[0:5])