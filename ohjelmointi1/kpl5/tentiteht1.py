luku = float(input("Anna luku"))
luvut = []
while luku >= 0:
    luvut.append(luku)
    luku = float(input("Anna luku"))

luvut.sort()
print(luvut)

if float(10) in luvut:
    print("Luku 10 löytyi")
else:
    print("Luku 10 ei löytynyt")

