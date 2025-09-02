loop = True
lista = []
while loop == True:
    luku = input("Anna kokonais luku, ja lopet painamalla ENTER tyhjään merkki jonoon")

    if luku != "":
        lista.append(int(luku))

    else:
        loop = False

tupla = []
for i in lista:
    testi = i in tupla
    if i >= 100 and testi == False:
        print(i)
        tupla.append(i)


#Tunnin alussa käydystä boolean esimerkistä suuri hyöty :)








