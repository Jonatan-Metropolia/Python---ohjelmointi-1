vuosi = int(input("Anna vuosiluku"))
chekki = vuosi/4
chekki2 = vuosi/100
chekki3 = vuosi/400

if chekki == int(chekki) or chekki2 == int(chekki2) and chekki3 == int(chekki3) :
    print(f"Vuosi {vuosi} on karkaus vuosi")
else:
    print(f"Vuosi {vuosi} ei ole karkaus vuosi")



