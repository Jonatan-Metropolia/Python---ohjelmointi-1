vuosi = int(input("Anna vuosiluku"))
chekki1 = vuosi/4
chekki2 = vuosi/100
chekki3 = vuosi/400
#if vuosi % 100 == 0 and vuosi % 400 == 0 or vuosi % 4 == 0:

if chekki1 != int(chekki1):
    print(f"Vuosi {vuosi} ei ole karkaus vuosi ")
else:
    print(f"Vuosi {vuosi} on karkaus vuosi")

