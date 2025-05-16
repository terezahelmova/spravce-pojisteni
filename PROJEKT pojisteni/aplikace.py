# Importy tříd z jiných souborů – správce pojištěných, rozhraní a třída pro jednotlivé pojištěné osoby
from spravce_pojisteni import SpravcePojisteni
from pojisteny import Pojisteny
from uzivatelske_rozhrani import UzivatelskeRozhrani

# Definice třídy Aplikace – hlavní logika běhu programu
class Aplikace:
    # Konstruktor – vytvoří instanci správce a rozhraní pro komunikaci s uživatelem
    def __init__(self):
        self.spravce = SpravcePojisteni()               # Spravuje seznam pojištěných
        self.ui = UzivatelskeRozhrani()                 # Zajišťuje komunikaci s uživatelem

    # Hlavní metoda, která spouští aplikaci a řídí její běh
    def spustit(self):
        bezi_aplikace = True                            # Řídicí proměnná pro hlavní smyčku

        while bezi_aplikace:
            self.ui.zobraz_menu()                       # Zobrazí menu s možnostmi
            volba = self.ui.ziskej_volbu()              # Získá volbu od uživatele
            bezi_aplikace = self.zpracuj_volbu(volba)   # Zpracuje volbu a rozhodne, zda pokračovat

    # Pomocná metoda pro zpracování jednotlivých voleb uživatele
    def zpracuj_volbu(self, volba):
        if volba == "1":
            self.vytvor_pojisteneho()                   # Přidání nového pojištěného
        elif volba == "2":
            seznam = self.spravce.vypis_pojistene()     # Výpis všech pojištěných
            self.ui.vypis_pojistene(seznam)
        elif volba == "3":
            self.vyhledej_pojisteneho()                 # Vyhledání pojištěného
        elif volba == "4":
            self.ui.zobraz_konec()                      # Ukončení programu
            return False
        else:
            self.ui.zobraz_neplatnou_volbu()            # Neplatná volba
        return True                                     # Pokračovat v aplikaci

    # Metoda pro vytvoření nové pojištěné osoby
    def vytvor_pojisteneho(self):
        jmeno, prijmeni = self.ui.ziskej_jmeno_a_prijmeni()  # Získání jména a příjmení
        vek = self.ui.ziskej_vek()                           # Získání a ověření věku
        telefon = self.ui.ziskej_telefon()                   # Získání telefonního čísla

        nova_osoba = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.spravce.pridej_pojisteneho(nova_osoba)          # Přidání osoby do seznamu
        self.ui.zobraz_zpravu_o_pridani()                    # Potvrzení přidání

    # Metoda pro vyhledání pojištěné osoby podle jména a příjmení
    def vyhledej_pojisteneho(self):
        jmeno, prijmeni = self.ui.ziskej_jmeno_a_prijmeni()  # Získání jména a příjmení
        nalezeni = self.spravce.najdi_pojisteneho(jmeno, prijmeni)
        self.ui.vypis_nalezeni(nalezeni)                     # Výpis výsledků hledání