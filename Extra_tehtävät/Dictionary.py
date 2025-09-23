grades = {"jukka":10}
loop = True
def grade_input():
    name= input("Anna oppilaan nimi")
    grade = int(input("Anna oppilaan arvosana"))
    grades[name]=grade

while loop == True:
    print(
        "1. Lisää oppilaan arvosana\n"
        "2. Tarkista oppilaan arvosana\n"
        "3. Lopeta ohjelma"
    )
    choise = int(input(""))
    if choise == 1:
        grade_input()
    elif choise == 2:
        checked = input("Anna oppilaan nimi")
        if checked in grades:
            print(grades[checked])
        else:
            print("Antamasi oppilas ei ollut listassa")
    elif choise == 3:
        loop = False
    else:
        print("Annoit väärän merkin, vain '1' tai '2' kelpaavat")

kokonais=0
amount=0
for i in grades.values():
    kokonais=kokonais + i
    amount=amount+1

keskiarvo = kokonais / amount
print(keskiarvo)
