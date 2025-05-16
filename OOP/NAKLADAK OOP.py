class Nakladak:

    def __init__(self):
         self.naklad = 0


    def naloz(self, hmotnost):
        self._naklad += hmotnost


    def vyloz(self, hmotnost):
        self._naklad -= hmotnost

    def vypis(self):
        print(f"Mám naloženo {self._naklad} kg.")

nakladak = Nakladak
nakladak.naloz(34)
nakladak.vyloz(6)
nakladak.vypis(nakladak.self)
print(nakladak.vypis)




