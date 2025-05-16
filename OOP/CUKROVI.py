class Cukrovi():
    # Třída reprezentuje cukroví

    barva = None
    tvar = None
    # Váha v gramech
    vaha = 0

    # Konstruktor
    def __init__(self, barva, tvar, vaha):
        self.barva = barva
        self.tvar = tvar
        self.vaha = vaha

    # Vrátí textovou reprezentaci cukroví
    def __str__(self):
        return f"Cukroví barvy {self.barva}, tvaru {self.tvar} a váhy {self.vaha} g"


cukrovi = Cukrovi


# Továrna na tvorbu cukroví
class TovarnaNaCukrovi():

    # Vytvoří banánové cukroví
    @staticmethod
    def vyrob_bananove():
        return Cukrovi("žlutá", "kulatý", 20)

    # Vytvoří jahodové cukroví
    @staticmethod
    def vyrob_jahodove():
        return Cukrovi("červená", "kulatý", 15)

    # Vytvoří čokoládové cukroví
    @staticmethod
    def vyrob_cokoladove():
        return Cukrovi("hnědá", "hranatý", 25)

tovarna_na_cukrovi = TovarnaNaCukrovi

for i in range(5):
        cukrovi = TovarnaNaCukrovi.vyrob_bananove()
        print(cukrovi)
for i in range(8):
        cukrovi = TovarnaNaCukrovi.vyrob_jahodove()
        print(cukrovi)
for i in range(12):
        cukrovi = TovarnaNaCukrovi.vyrob_cokoladove()
        print(cukrovi)
