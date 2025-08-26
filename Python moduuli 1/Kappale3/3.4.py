vuosi = int(input("Anna vuosiluku"))
chekki1 = vuosi/4
chekki2 = vuosi/100
chekki3 = vuosi/400

if chekki1 != int(chekki1) or chekki2 != int(chekki2) and chekki3 != int(chekki3):
    print(f"Vuosi {vuosi} ei ole karkaus vuosi ")
else:
    print(f"Vuosi {vuosi} on karkaus vuosi")

