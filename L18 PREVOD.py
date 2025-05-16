def prevedCisloNaZnak(cislo):
    if (cislo >= 0 and cislo <= 9):
        return chr(cislo + ord('0'));
    else:
        return chr(cislo - 10 + ord('A'));


# Funkce převádí číslo z desítkové soustavy na
# zvolenou jinou soustavu
def fromDeci(vysledek, baze, zadaneCislo):
    # Cyklus opakovaně dělí zadané desítkové číslo
    # zadanou bází (typem soustavy, do níž chce uživatel
    # zadané číslo převést)
    while (zadaneCislo > 0):
        vysledek += prevedCisloNaZnak(zadaneCislo % baze);
        zadaneCislo = int(zadaneCislo / baze);

    # hodnotu výsledku je nutné převrátit
    vysledek = vysledek[::-1];

    return vysledek;


# Funkce nacte od uživatele číslo, které chce převést.
# Načtené číslo musí být kladný integer.
def nactiCislo(text_zadani, text_chyba):
    spatne = True
    while spatne:
        try:
            nacteneCislo = int(input(text_zadani))
            if nacteneCislo < 0:
                print("Zadané číslo musí být nezáporné!\n")
                continue
            spatne = False
        except ValueError:
            print(text_chyba)
        else:
            return nacteneCislo

        # Funkce nacte od uivatele číslo soustavy, na kterou che převést.


# Načtené číslo musí být kladný integer.
def nactiBazi(text_zadani, text_chyba):
    spatne = True
    while spatne:
        try:
            nactenaBaze = int(input(text_zadani))
            if nactenaBaze < 0:
                print("Zadané číslo musí být nezáporné!\n")
                continue
            if nactenaBaze < 2 or nactenaBaze > 16:
                print("Zadané číslo musí v rozmezí 2-16!\n")
                continue
            spatne = False
        except ValueError:
            print(text_chyba)
        else:
            return nactenaBaze

        # Hlavní program


zadaneCislo = nactiCislo("Číslo v desítkové soustavě: ", "Neplatné číslo!\n");
baze = nactiBazi("Číselná soustava (2-16): ", "Neplatné zadání!\n");
vysledek = "";
print("Číslo ve zvolené soustavě:", fromDeci(vysledek, baze, zadaneCislo));