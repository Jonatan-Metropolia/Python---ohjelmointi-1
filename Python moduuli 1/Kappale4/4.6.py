import random
sisälle=0
#ulkona=0
n=float(input("Likiarvo testauksien lukumäärä"))
loop=0
while loop <= n:
    x = random.uniform (-1,1)
    y = random.uniform (-1,1)
    loop = loop +1
    if x*x+y*y<1:
        sisälle = sisälle +1
    #else:
        #ulkona = ulkona+1

suhde = 4*sisälle/loop

print(f"Likimääräinen Pi = {suhde} ")



