class Lokace():
    # Třída reprezentuje lokaci

    sever   = None # Lokace na severu
    jih     = None # Lokace na jihu
    zapad   = None # Lokace na západě
    vychod  = None # Lokace na východě

    nazev   = None # Název lokace
    popis   = None # Dlouhý popis lokace

    def __init__(self, nazev, popis):
        self.nazev = nazev
        self.popis = popis

    def __str__(self):
        vystup = ( self.nazev + "\n"
                 + self.popis + "\n\n")
        smery = ""
        if self.sever:
            smery += "sever "
        if self.jih:
            smery += "jih "
        if self.zapad:
            smery += "západ "
        if self.vychod:
            smery += "východ "
        vystup += f"Můžeš jít na {smery}\n"
        return vystup


lokace = Lokace


class Hra():
    hrad = Lokace("Hrad",
                  "Stojíš před okovanou branou gotického hradu, která je zřejmě jediným vchodem do pevnosti. Klíčová dírka je pokryta pavučinami, což vzbuzuje dojem, že je budova opuštěná.")
    les1 = Lokace("Les",
                  "Jsi na lesní cestě, která se klikatí až za obzor, kde mizí v siluetě zapadajícího slunce. Ticho podvečerního lesa občas přeruší zpěv posledních ptáků.")
    les2 = Lokace("Lesní rozcestí", "Nacházíš se na lesním rozcestí.")
    les3 = Lokace("Les",
                  "Jsi na lesní cestě, která se klikatí až za obzor, kde mizí v siluetě zapadajícího slunce. Ticho podvečerního lesa občas přeruší zpěv posledních ptáků.")
    rybnik = Lokace("Rybník",
                    "Došel jsi ke břehu malého rybníka. Hladina je v bezvětří jako zrcadlo. Kousek od tebe je dřevěná plošina se stavidlem.")
    les4 = Lokace("Les",
                  "Jsi na lesní cestě, která se klikatí až za obzor, kde mizí v siluetě zapadajícího slunce. Ticho podvečerního lesa občas přeruší zpěv posledních ptáků.")
    dum = Lokace("Dům",
                 "Stojíš před svým rodným domem, citíš vůni čerstvě nasekaného dřeva, která se line z hromady vedle vstupních dvěří.")

    # Propojení lokací
    hrad.vychod = les1
    les1.zapad = hrad
    les1.vychod = les2
    les2.zapad = les1
    les2.vychod = les3
    les2.jih = les4
    les3.zapad = les2
    les3.vychod = rybnik
    rybnik.zapad = les3
    les4.sever = les2
    les4.vychod = dum
    dum.zapad = les4
    # Uložení aktuální lokace
    aktualni_lokace = dum

    # Zpracuje textová příkaz
    def zpracuj_prikaz(self, prikaz):
        prikaz = prikaz.lower()
        if prikaz.startswith("jdi"):

            if prikaz.endswith("sever") and self.aktualni_lokace.sever:
                self.aktualni_lokace = self.aktualni_lokace.sever
            elif prikaz.endswith("jih") and self.aktualni_lokace.jih:
                self.aktualni_lokace = self.aktualni_lokace.jih
            elif prikaz.endswith("západ") and self.aktualni_lokace.zapad:
                self.aktualni_lokace = self.aktualni_lokace.zapad
            elif prikaz.endswith("východ") and self.aktualni_lokace.vychod:
                self.aktualni_lokace = self.aktualni_lokace.vychod
            else:
                print("Tímto směrem nelze jít.")

        elif prikaz != "konec":
            print("Můj vstupní slovník neobsahuje tento příkaz.")

    # Vrátí aktuální lokaci
    def vrat_auktualni_lokaci(self):
        return self.aktualni_lokace

hra = Hra

# print("Tato aplikace vznikla jako cvičení k použití referencí. Můžeš procházet světem pomocí textových příkazů, jako jdi na sever a podobně. Aplikaci ukončíš příkazem konec. \n")
hra = Hra()
prikaz = ""

while prikaz.lower() != "konec":
    print(hra.vrat_auktualni_lokaci())
    print("Zadej příkaz: ", end="")
    prikaz = input()
    hra.zpracuj_prikaz(prikaz)