luku = int(input("Anna tasaluku"))
alkuluku = True

for i in range(2,int(luku*0.5+1)):
    if luku % i == 0:
        alkuluku = False
        print(f"{luku}/{i}=", luku/i)
        break


if alkuluku == True:
    print("Luku on alkuluku")
elif alkuluku == False:
    print("Luku ei ole alkuluku")










