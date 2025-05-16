import random

class GenerátorVět:
    def __init__(self):
        # Seznamy pro jednotlivé části vět
        self.podmety = ["jednorožec", "programátor", "manažer", "hroch", "T-rex"]
        self.prisudky = ["spal", "ležel", "vařil", "uklízel", "derivoval"]
        self.privlastky = ["modrý", "velký", "hubený", "nejlepší", "automatizovaný"]
        self.prislovce = ["rychle", "s oblibou", "hodně", "málo", "se zpožděním"]
        self.prislovecna_urceni_mista = ["pod stolem", "v lese", "u babičky", "v práci", "na stole"]

    def vygeneruj_vetu(self):
        # Vytvoření náhodné věty
        podmet = random.choice(self.podmety)
        prisudek = random.choice(self.prisudky)
        privlastek = random.choice(self.privlastky)
        prislovce = random.choice(self.prislovce)
        prislovecna_urceni = random.choice(self.prislovecna_urceni_mista)

        veta = f"{podmet.capitalize()} {privlastek} {prisudek} {prislovce} {prislovecna_urceni}."
        return veta

# Vytvoření instance generátoru
generátor = GenerátorVět()

# Vygenerování a vypsání 10 vět
for _ in range(10):
    print(generátor.vygeneruj_vetu())