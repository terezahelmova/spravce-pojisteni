# Nadtrieda (Superclass)
class Zivocich:
    def __init__(self, meno, vek):
        self.meno = meno
        self.vek = vek

    def predstavit_sa(self):
        print(f"Som zivocich s menom {self.meno} a vekom {self.vek} rokov.")

# Podtrieda (Subclass)
class Pes(Zivocich):
    def __init__(self, meno, vek, plemeno):
        # Volanie konštruktora nadtriedy
        super().__init__(meno, vek)
        self.plemeno = plemeno

    def zvuk(self):
        print("Haf! Haf!")

# Podtrieda (Subclass)
class Macka(Zivocich):
    def __init__(self, meno, vek, farba):
        # Volanie konštruktora nadtriedy
        super().__init__(meno, vek)
        self.farba = farba

    def zvuk(self):
        print("Mňau! Mňau!")

# Vytvorenie inštancií podtried
pes1 = Pes("Rex", 3, "Nemecký ovčiak")
macka1 = Macka("Micka", 2, "čierna")

# Volanie metód nadtriedy a podtried
pes1.predstavit_sa()
pes1.zvuk()

macka1.predstavit_sa()
macka1.zvuk()