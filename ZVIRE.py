class Zvíře:
    def __init__(self, jméno):
        self.jméno = jméno

    def mluv(self):
        return ""

    def __str__(self):
        return f"{self.__class__.__name__}: {self.jméno}"


class Pes(Zvíře):
    def mluv(self):
        return "Haf!"


class Kočka(Zvíře):
    def mluv(self):
        return "Mňau!"


class Kachna(Zvíře):
    def mluv(self):
        return "Kvak!"


# Vytvoření pole se zvířaty
zvirata = [Pes("Rex"), Kočka("Micka"), Kachna("Donald")]

# Výpis zvuků zvířat
for zvire in zvirata:
    print(f"{zvire.jméno} říká: {zvire.mluv()}")

# Výpis instancí zvířat
for zvire in zvirata:
    print(zvire)
