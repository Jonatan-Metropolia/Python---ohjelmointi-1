def muunnos(gallona):
    litra = float(gallona)*3.785
    return litra

loop = True

while loop == True:
    ammount = input("Montako gallonaa haluat litroiksi?")

    if float(ammount) >= 0:
        litra = muunnos(ammount)
        print(f"{litra:.3f} litraa")
    else:
        loop = False





