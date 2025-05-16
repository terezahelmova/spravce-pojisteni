class Uzivatel:

    def __init__(self, jmeno, heslo):
        self._jmeno = jmeno
        self._heslo = heslo
        self._prihlaseny = False

    def prihlas_se(self, zadane_jmeno, zadane_heslo):
        if self._jmeno == zadane_jmeno and self._heslo == zadane_heslo:
            self._prihlaseny = True
            return True
        else:
            self._prihlaseny = False
            return False  # jméno nebo heslo nesouhlasí