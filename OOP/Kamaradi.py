class Clovek():
    # Třída reprezentuje člověka, který má jméno, věk a kamaráda
    jmeno = None
    vek = None
    kamarad = None

    def predstav_se(self):
        print(f"Ahoj, já jsem {self.jmeno}, je mi {self.vek} let a můj kamarád je {self.kamarad.jmeno}")

from clovek import Clovek


        karel = Clovek()
        karel.jmeno = "Karel Novák"
        karel.vek = 33
        josef = Clovek()
        josef.jmeno = "Cyril Nový"
        josef.vek = 27

        # Spřátelení
        karel.kamarad = josef
        josef.kamarad = karel

        # Představení
        karel.predstav_se()
        josef.predstav_se()