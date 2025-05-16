import math

class Prevodnik():
    #Obsahuje pomocné metody pro převod mezi radiány a stupni

    #Převede radiány na stupně
    @staticmethod
    def radiany_na_stupne(radiany):
        return math.degrees(radiany)

    #Převede stupně na radiány
    @staticmethod
    def stupne_na_radiany(stupne):
        return math.radians(stupne)

prevodnik = Prevodnik

print(f"6.28 radiánů na stupně: {Prevodnik.radiany_na_stupne(6.28)}")
print(f"90 stupňů na radiány: {Prevodnik.stupne_na_radiany(90)}")