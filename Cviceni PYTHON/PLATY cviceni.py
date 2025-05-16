platy = input().split(",")

soucet = 0
print(platy)
for i in range(len(platy)):
    soucet += int(platy[i])

    print(f"Průměr platu je: {soucet/len(platy)}")
    