import random

class Generator:
    podmety = ["jednorožec", "programátor", "manažer", "hroch", "T-rex"]
    prisudky = ["spal", "ležel", "vařil", "uklízel", "derivoval"]
    privlastky = ["modrý", "velký", "hubený", "nejlepší", "automatizovaný"]
    prislovce = ["rychle", "s oblibou", "hodně", "málo", "se zpožděním"]
    pum = ["pod stolem", "v lese", "u babičky", "v práci", "na stole"]

    def generuj(cls):
        podmet = random.choice(cls.podmety)
        prisudek = random.choice(cls.prisudky)
        privlastek = random.choice(cls.privlastky)
        prislovce = random.choice(cls.prislovce)
        pum = random.choice(cls.pum)

        veta = f"{privlastek} {podmet} {prislovce} {prisudek} {pum}"
        return veta

generator = Generator()

for _ in range(10):
    veta = generator.generuj()
    print(veta)