
def laskuri(luvut):
    kerto= luvut[0]*luvut[1]*luvut[2]
    summa= luvut[0]+luvut[1]+luvut[2]
    k_arvo= summa/len(luvut)
    return kerto, summa, k_arvo

luvut=[]
for i in range(3):
    luvut.append(float(input("Anna luku")))

(kerto, summa, k_arvo) = laskuri(luvut)
print(f"Kerrottuna = {kerto:.3f}\n"
      f"Summa = {summa:.3f}\n"
      f"k_arvo = {k_arvo:.3f}")


