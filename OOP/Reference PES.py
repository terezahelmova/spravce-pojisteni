class Osoba():

    jmeno = None
    pes = None

    def __init__(self, jmeno):
        self.jmeno = jmeno


class Pes():
    # Třída reprezentuje psa

    jmeno = None
    vek = 1

    # Konstruktor
    def __init__(self, jmeno):
        self.jmeno = jmeno

    # Nechá psa zestárnout o rok
    def zestarni(self):
        self.vek += 1

    # Vrátí textovou reprezentaci psa
    def __str__(self):
        return f"{self.jmeno} ({self.vek})"


osoba = Osoba
pes = Pes

karel = Osoba("Karel Novák")
lenka = Osoba("Lenka Nováková")
azor = Pes("Azor")
karel.pes = azor
lenka.pes = azor
print(azor)

# Zestárnutí psa
karel.pes.zestarni()
lenka.pes.zestarni()

# Kontrolní výpis dat
print(azor)