class Clovek:  # Správná definice třídy
    def __init__(self, jmeno):  # Konstruktor pro inicializaci jména
        self.jmeno = jmeno
        self.vek = vek

    def pozdrav(self):  # Opravená metoda
        print(f"Ahoj, já jsem {self.jmeno}!")

# Vytvoření instance třídy Clovek
Karel = Clovek("Karel")
Karel.vek = 42
Karel.pozdrav()

