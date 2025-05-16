
print("Výpočet průměru známek")
print("Zadejte známky oddělené čárkou: ")


vstup = input()


znamky = vstup.split(",")

# Parsování známek
soucet = 0
for znamka in znamky:
    soucet += int(znamka.strip())  # přidáno 'strip()' pro odstranění bílých znaků

prumer = soucet / len(znamky)


print(f"Průměr: {prumer}")
