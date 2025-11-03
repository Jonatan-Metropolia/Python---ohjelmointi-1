'''
Koodi kertoo kaikki parilliset luvut käyttäjän antamaan lukuun asti
Jos luku on negatiivinen tai 0 niin virhe ilmoitus ilmenee
'''

loppu = int(input("Anna kokonais luku"))

if loppu <=0:
    print("Virhe!, anna positiivinen luku joka on ismopi kuin 0")
else:
    for i in range(2,loppu+1,2):
        print(i)
