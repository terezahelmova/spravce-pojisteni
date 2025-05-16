# Třída UzivatelskeRozhrani se stará o veškerou komunikaci s uživatelem (vstupy a výpisy)

class UzivatelskeRozhrani:
    # Zobrazí hlavní menu aplikace
    def zobraz_menu(self):
        print("\n--- Evidence pojištěných ---")
        print("1. Přidat nového pojištěného")
        print("2. Vypsat všechny pojištěné")
        print("3. Vyhledat pojištěného")
        print("4. Konec\n")

    # Získá volbu od uživatele
    def ziskej_volbu(self):
        return input("Vyberte možnost: ")

    # Získá jméno a příjmení – společná metoda
    def ziskej_jmeno_a_prijmeni(self):
        jmeno = self.ziskej_neprazdny_vstup("Zadejte jméno: ")
        prijmeni = self.ziskej_neprazdny_vstup("Zadejte příjmení: ")
        return jmeno, prijmeni

    # Získá věk – kontroluje, že je to číslo větší než 0
    def ziskej_vek(self):
        while True:
            try:
                vek = int(input("Zadejte věk: "))
                if vek > 0:
                    return vek
                else:
                    print("Věk musí být kladné číslo.")
            except ValueError:
                print("Zadejte platné číslo.")

    # Získá telefonní číslo (bez validace formátu)
    def ziskej_telefon(self):
        return input("Zadejte telefonní číslo: ")

    # Pomocná metoda pro získání neprázdného vstupu
    def ziskej_neprazdny_vstup(self, vyzva):
        while True:
            hodnota = input(vyzva).strip()
            if hodnota:
                return hodnota
            print("Tato hodnota nesmí být prázdná!")

    # Vypíše zadaný seznam pojištěných osob
    def vypis_pojistene(self, seznam):
        if seznam:
            print("\nSeznam pojištěných:")
            for osoba in seznam:
                print(osoba)
        else:
            print("\nŽádní pojištění nejsou evidováni.")

    # Vypíše nalezené osoby při hledání
    def vypis_nalezeni(self, nalezeni):
        if nalezeni:
            print("\nNalezení pojištěného:")
            for osoba in nalezeni:
                print(osoba)
        else:
            print("\nPojištěný nebyl nalezen.")

    # Zobrazí zprávu při úspěšném přidání osoby
    def zobraz_zpravu_o_pridani(self):
        print("Pojištěný byl přidán.")

    # Zobrazí zprávu o ukončení programu
    def zobraz_konec(self):
        print("Ukončuji aplikaci.")

    # Zobrazí chybu při neplatné volbě
    def zobraz_neplatnou_volbu(self):
        print("Neplatná volba. Zkuste to znovu.")