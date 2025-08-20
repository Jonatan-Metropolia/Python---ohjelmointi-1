leiviskä = input('Anna leiviskät')
naula = input('Anna naulat')
luoti = input('Anna luodit')

gramma = float(luoti)*13.3+float(naula)*32*13.3+float(leiviskä)*20*32*13.3
kilo = int(gramma)/1000
loputgrammat = gramma-round(kilo, 1)*1000
print("Kilot " + f"{kilo:.0f}")
print("Grammat " + f"{loputgrammat:.2f}")