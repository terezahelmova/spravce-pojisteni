class Zdravic:
    text = "Ahoj"
    def pozdrav(self, jmeno):
        return f"{self.text} {jmeno}!"

zdravic = Zdravic()
zdravic.text = "Ahoj uživateli"
print(zdravic.pozdrav("Karel"))
print(zdravic.pozdrav("Petr"))
zdravic.text = "Vítám tě tu programátore"
print(zdravic.pozdrav("Richard"))
zdravic = Zdravic()
zdravic.pozdrav()




class Zdravic:
    """
    Třída reprezentuje zdravič, který slouží ke zdravení uživatelů.
    """

    text = "Ahoj"
    """
    Atribut obsahující výchozí text pozdravu. Pokud není specifikován jiný text,
    použije se tento výchozí text při sestavování pozdravu.
    """

    def pozdrav(self, jmeno):
        """
        Vrátí pozdrav uživatele s nastaveným textem a jeho jménem.

        Parametry:
        - jmeno (str): Jméno osoby, kterou chceme pozdravit.

        Výstup:
        - str: Text pozdravu s jménem osoby.
        """
        return f"{self.text} {jmeno}!"






