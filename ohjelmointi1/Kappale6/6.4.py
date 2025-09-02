def luvut(lista):
    tallennus = 0
    for i in lista:
        summa = tallennus + i
        tallennus = summa

    return tallennus

numbers = [1, 7, 9, 4]


print(luvut(numbers))



