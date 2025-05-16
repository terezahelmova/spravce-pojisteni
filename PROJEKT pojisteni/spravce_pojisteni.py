# Třída, která spravuje seznam pojištěných osob
class SpravcePojisteni:
    # Konstruktor – vytvoří prázdný seznam pojištěných
    def __init__(self):
        self.seznam_pojistenych = []

    # Metoda pro přidání nové pojištěné osoby do seznamu
    def pridej_pojisteneho(self, pojisteny):
        self.seznam_pojistenych.append(pojisteny)

    # Metoda pro vrácení celého seznamu pojištěných
    def vypis_pojistene(self):
        return self.seznam_pojistenych

    # Metoda pro vyhledání osoby podle jména a příjmení (nezávisle na velikosti písmen)
    def najdi_pojisteneho(self, jmeno, prijmeni):
        return [osoba for osoba in self.seznam_pojistenych
                if osoba.jmeno.lower() == jmeno.lower() and osoba.prijmeni.lower() == prijmeni.lower()]