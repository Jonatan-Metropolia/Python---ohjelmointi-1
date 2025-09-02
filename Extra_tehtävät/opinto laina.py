import numpy as np
import matplotlib.pyplot as plt

# Parametrit
laina_vuosi = 4500
vuodet = 4
kokonaislaina = laina_vuosi * vuodet

euribor = 0.035
marginaali_normi = 0.005
marginaali_akava = 0.0  # 0 % ensimmäiset 5 vuotta
korko_normi = euribor + marginaali_normi
korko_akava = euribor + marginaali_akava

# Nostomaksut
def nostomaksut(nostot_vuodessa, akava=False):
    if akava:
        return 0
    yhteensa = 30 + (nostot_vuodessa*vuodet - 1)*5
    return yhteensa

# Lasketaan korkokustannukset (vain 4 vuoden opiskeluaikana)
def laske_korot(nostot_vuodessa, akava=False):
    kuukausi_korko = (korko_akava if akava else korko_normi)/12
    kuukausia = vuodet*12
    lainan_osuus = laina_vuosi / nostot_vuodessa  # noston määrä
    korot = 0
    for vuosi in range(vuodet):
        for nosto in range(nostot_vuodessa):
            kk = vuosi*12 + int((12/nostot_vuodessa)*nosto)
            kuukausia_jaljella = kuukausia - kk
            korot += lainan_osuus * kuukausi_korko * kuukausia_jaljella
    return korot

# Laskenta
nostot = np.arange(1, 21)
kokonais_normi = [laske_korot(n, akava=False) + nostomaksut(n, akava=False) for n in nostot]
kokonais_akava = [laske_korot(n, akava=True) + nostomaksut(n, akava=True) for n in nostot]

# Piirto
plt.style.use("seaborn-v0_8")
plt.figure(figsize=(10,6))

plt.plot(nostot, kokonais_normi, label="Ilman Akava-etua (korot+maksut)",
         color="red", marker="o")
plt.plot(nostot, kokonais_akava, label="Akava-etu (korot+maksut)",
         color="green", marker="s")

plt.xlabel("Nostot vuodessa")
plt.ylabel("Kustannus 4 vuodessa (€)")
plt.title("Opintolainan kokonaiskustannus eri nostotiheyksillä (4 v aikana, 18 000 €)")
plt.xticks(nostot)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)

# Annotoinnit: minimi kummallekin käyrälle
min_normi = min(zip(nostot, kokonais_normi), key=lambda x: x[1])
min_akava = min(zip(nostot, kokonais_akava), key=lambda x: x[1])

plt.annotate(f"Min {min_normi[1]:.0f} €",
             xy=min_normi, xytext=(min_normi[0]+1, min_normi[1]+80),
             arrowprops=dict(arrowstyle="->", color="red"), color="red")

plt.annotate(f"Min {min_akava[1]:.0f} €",
             xy=min_akava, xytext=(min_akava[0]+1, min_akava[1]+80),
             arrowprops=dict(arrowstyle="->", color="green"), color="green")

plt.show()
