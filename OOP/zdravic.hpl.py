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