dny = ["PO", "ÚT", "ST", "CT", "PA", "SO", "NE"]

den = int(input())
if den <1 and den > 7:
    print("Zadejste hodnotu mezi 1 a 7")
else:
    print(dny[den-1])
