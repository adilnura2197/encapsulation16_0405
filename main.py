class Sportchi:
    def __init__(self, ism, ochko):
        self.ism = ism
        self.ochko = ochko

    def gol_ur(self):
        self.ochko += 1
        print("Gol urildi!")

    def info(self):
        print(f"Ism: {self.ism}")
        print(f"Ochko: {self.ochko}")


s1 = Sportchi("Ali", 5)

s1.info()
s1.gol_ur()
s1.info()
