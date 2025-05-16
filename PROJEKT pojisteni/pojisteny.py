# Definice třídy Pojisteny, která reprezentuje jednu pojištěnou osobu
class Pojisteny:
    # Konstruktor třídy – nastaví jméno, příjmení, věk a telefon osoby
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno              # Křestní jméno
        self.prijmeni = prijmeni        # Příjmení
        self.vek = vek                  # Věk (v letech)
        self.telefon = telefon          # Telefonní číslo

    # Speciální metoda pro převod objektu na textový řetězec
    # Používá se např. při výpisu objektu (print)
    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, {self.vek} let, Telefon: {self.telefon}"
