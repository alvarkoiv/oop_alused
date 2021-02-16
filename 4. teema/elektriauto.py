from Auto import Auto
class elektriauto(Auto):
    def __init__(self, t, m, a):
        Auto().__init__(t, m, a)
        self.aku_suurus = 50

    def aku_kirjeldus(self):
        print("Antud auto sisaldab " + str(self.aku_suurus) + " patareid.")