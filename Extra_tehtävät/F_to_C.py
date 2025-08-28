#F=C*(9/5)+32
#C=(F-32)/(9/5)
stop = 0
print("F = fahrenheit to celcius ja C = celsius to fahrenheit")
print('Voit halutessasi pysäyttöö ohjelman valittuasi yksikön painamalla "ENTER" tyhjään vastaus ruutuun')
unit = str(input('Anna lämpötila yksikkö "C" tai "F"'))



if unit == "C":
    while stop ==0:
        temp = input("Anna lämpötila muodossa xx.xx: ")

        if temp == "":
            stop = 1

        if temp != "":
            C = float(temp)
            F = C*(9/5)+32
            print(f"{C} C = {F} F")
elif unit == "F":
    while stop ==0:
        temp = input("Anna lämpötila muodossa xx.xx: ")

        if temp == "":
            stop = 1

        if temp != "":
            F = float(temp)
            C=(F-32)/(9/5)
            print(f"{F:.3f}F = {C:.3f}C")
else:
    print('Annoit väärän syötteen, hyväksyttävä arvo on "F" tai "C"')

print("Ohjelma loppui")


