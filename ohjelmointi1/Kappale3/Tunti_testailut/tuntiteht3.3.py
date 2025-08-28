math = int(input("Anna matikan numero"))
chem = int(input("Anna kemian numero"))
phy = int(input("Anna fysiikan numero"))
if math < 50 or chem < 50 or phy < 50:
    print("Hylätty")
elif math > 90 and phy > 90:
    print("Stipendi saatu")
elif chem > 95:
    print("Stipendi saatu")
else:
    print("Hylätty")

