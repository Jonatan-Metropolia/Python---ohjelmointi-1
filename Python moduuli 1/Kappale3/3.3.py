sukupuoli = str(input("Anna sukupuoli"))
hemoglobiini = float(input("Anna hemoglobiini"))

if sukupuoli == str("mies") and 134<=hemoglobiini<=195:
    print("Hemoglobiini on normaali")
elif sukupuoli == str("mies") and hemoglobiini<134:
    print("Hemoglobiini liian matala")
elif sukupuoli == str("mies") and hemoglobiini>195:
    print("Hemoglobiini on liian korkea")

if sukupuoli == str("nainen") and 117<=hemoglobiini<=175:
    print("Hemoglobiini on normaali")
elif sukupuoli == str("nainen") and hemoglobiini<117:
    print("Hemoglobiini on liian matala")
elif sukupuoli == str("nainen") and hemoglobiini>175:
    print("Hemoglobiini on liian korkea")

