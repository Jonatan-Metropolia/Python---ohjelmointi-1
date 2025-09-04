
def metrihinta(diam, price):
    true_price2 = price/(((3.14 * (diam / 2) ** 2))/10000)
    return true_price2



def vertailu():
    a = metrihinta(diam_pizza1, price_pizza1)
    b = metrihinta(diam_pizza2, price_pizza2)
    if a<b:
        print(f"Ensimmäinen pizza on halvempi, sen hinta = {a}€/m^2 ja toisen on {b}€/m^2")
    else:
        print(f"Toinen pizza on halvempi, sen hinta = {b}€/m^2 ja toisen on {a}€/m^2")



diam_pizza1= float(input("Anna ensimmäisen pizzan halkaisija (cm) muodossa xx.xx"))
price_pizza1= float(input("Anna ensimmäisen pizzan hinta (€)"))

diam_pizza2= float(input("Anna toisen pizzan halkaisija (cm) muodossa xx.xx"))
price_pizza2= float(input("Anna toisen pizzan hinta (€)"))

vertailu()
#