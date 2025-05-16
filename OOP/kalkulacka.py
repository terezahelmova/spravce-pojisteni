class Kalkulacka:
    def zadej_cisla(self):  # definice metody pro získání vstupů
        self.a = float(input("Zadej 1. číslo:\n"))
        self.b = float(input("Zadej 2. číslo:\n"))

    def proved_operaci(self): # definice metody pro základní matematiské operace
            self.scitani = self.a + self.b
            self.odcitani = self.a - self.b
            self.nasobeni = self.a * self.b
            self.deleni = self.a / self.b

    def zobraz_vysledek(self):   #definice metody pro zobrazení výsledků
            print(f"Součet: {self.scitani}")
            print(f"Rozdíl: {self.odcitani}")
            print(f"Součin: {self.nasobeni}")
            print(f"Podíl: {self.deleni}")

kalkulacka = Kalkulacka()
kalkulacka.zadej_cisla()
kalkulacka.proved_operaci()
kalkulacka.zobraz_vysledek()

