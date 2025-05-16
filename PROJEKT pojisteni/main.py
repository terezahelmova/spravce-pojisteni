# Import hlavní třídy Aplikace z modulu aplikace
from aplikace import Aplikace

# Tento blok zajistí, že se následující kód spustí jen při přímém spuštění souboru,
# ne při importu z jiného souboru
if __name__ == "__main__":
    aplikace = Aplikace()      # Vytvoření instance aplikace
    aplikace.spustit()         # Spuštění hlavní metody aplikace (zobrazí menu a řídí celý běh programu)

