class Kostka:
    """
    Třída reprezentuje hrací kostku.
    """

    def __init__(self,pocet_sten=6):
        self._pocet_sten = pocet_sten

    def vrat_pocet_sten(self):
        """
        Vrátí počet stěn kostky.
        """
        return self._pocet_sten

    def hod(self):
        """
        Vykoná hod kostkou a vrátí číslo od 1 do
        počtu stěn.
        """
        import random as _random
        return _random.randint(1, self._pocet_sten)

    def __str__(self):
        """
        Vrací textovou reprezentaci kostky.
        """
        return f"Kostka({self._pocet_sten})"

class Bojovnik:
    """
    Třída reprezentující bojovníka do arény.
    """

    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        """
        jmeno - jméno bojovníka
        zivot - maximální život bojovníka
        utok - útok bojovníka
        obrana - obrana bojovníka
        kostka - instance kostky
        """
        self._jmeno = jmeno
        self._zivot = zivot
        self._max_zivot = zivot
        self._utok = utok
        self._obrana = obrana
        self._kostka = kostka
        self._zprava = ""

    def __str__(self):
        return str(self._jmeno)

    def je_nazivu(self):
        return self._zivot > 0

    def graficky_zivot(self):
        celkem = 20
        pocet = int(self._zivot / self._max_zivot * celkem)
        if pocet == 0 and self.je_nazivu():
            pocet = 1
        return f"[{'#' * pocet}{' ' * (celkem - pocet)}]"

    def bran_se(self, uder):
        zraneni = uder - (self._obrana + self._kostka.hod())
        if zraneni > 0:
            zprava = f"{self._jmeno} utrpěl poškození {zraneni} hp."
            self._zivot = self._zivot - zraneni
            if self._zivot < 0:
                self._zivot = 0
                zprava = f"{zprava[:-1]} a zemřel."
        else:
            zprava = f"{self._jmeno} odrazil útok."
        self._nastav_zpravu(zprava)

    def utoc(self, souper):
        uder = self._utok + self._kostka.hod()
        zprava = f"{self._jmeno} útočí s úderem za {uder} hp."
        self._nastav_zpravu(zprava)
        souper.bran_se(uder)

    def _nastav_zpravu(self, zprava):
        self._zprava = zprava

    def vrat_posledni_zpravu(self):
        return self._zprava

kostka = Kostka
bojovnik = Bojovnik

kostka = Kostka(10)
bojovnik = Bojovnik("Zalgoren", 100, 20, 10, kostka)
print("Život: {0}".format(bojovnik.graficky_zivot())) #test graficky_zivot()
#útok na našeho bojovníka
souper = Bojovnik("Shadow", 60, 18, 15, kostka)
souper.utoc(bojovnik)
print(souper.vrat_posledni_zpravu())
print(bojovnik.vrat_posledni_zpravu())
print("Život: {0}".format(bojovnik.graficky_zivot()))
