class Kostka:

    def __init__(self,pocet_sten=6):
        self.__pocet_sten = pocet_sten

    def vrat_pocet_sten(self):
        """
        Vrátí počet stěn kostky.
        """
        return self.__pocet_sten

    def __str__(self):
        """
        Vrací textovou reprezentaci kostky.
        """
        return str(f"Kostka s {self.__pocet_sten} stěnami.")

desetistenna = Kostka(10)

print(f"Před pokusem o úpravu privátního atributu: {desetistenna}")
desetistenna.__pocet_sten = 365
print(f"Upravili jsme atribut na hodnotu: {desetistenna.__pocet_sten}")
print(f"Po pokusu o úpravu privátního atributu: {desetistenna}")
