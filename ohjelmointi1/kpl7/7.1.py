
kuukausi = int(input("Anna kuukausi"))

luvut = [(12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]

talvi, kevät, kesä, syksy = luvut

if kuukausi in talvi:
    print("talvi")
elif kuukausi in kevät:
    print ("kevät")
elif kuukausi in kesä:
    print("kesä")
elif kuukausi in syksy:
    print("syksy")
