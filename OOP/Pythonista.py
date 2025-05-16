class Clovek():
    # Třída reprezentuje člověka

    jmeno = None
    vek = None
    unava = 0

    # Konstruktor
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    # Spí danou dobu
    def spi(self, doba):
        self.unava -= doba * 10
        if self.unava < 0:
            self.unava = 0

    # Uběhne danou vzdálenost
    def behej(self, vzdalenost):
        if self.unava + vzdalenost <= 20:
            self.unava += vzdalenost
        else:
            print("Jsem příliš unavený")

    # Vrátí textovou reprezentaci člověka
    def __str__(self):
        return f"{self.jmeno} {self.vek}"
clovek = Clovek

class Pythonista(Clovek):
    # Třída reprezentuje Pythonistu

    # Integrované vývojové prostředí, ve kterém Pythonista píše kód
    ide = None

    def __init__(self, jmeno, vek, ide):
        super(Pythonista, self).__init__(jmeno, vek)
        self.ide = ide

    def programuj(self, pocet_radku):
        if pocet_radku < 10:
            pocet_radku = 10
        if self.unava + pocet_radku / 10 <= 20:
            self.unava += pocet_radku / 10
        else:
            print("Jsem příliš unavený, abych programoval")

pythonista = Pythonista

karel = Pythonista("Karel Nový", 25, "VSCode")
print(karel)
karel.behej(10)
karel.behej(10)
karel.programuj(5)
karel.behej(10)
karel.spi(8)
karel.programuj(100)





