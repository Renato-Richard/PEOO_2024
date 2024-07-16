class Circulo():
    def __init__ (self):
        self.__raio = 0
    def set(self, v):
        if self.__raio > 0: self.__raio == v
        else: raise ValueError()
    def get(self):
        return self.__raio
    def calc_a(self):
        return 3.14 * self.__raio ** 2 
    def calc_c(self):
        return 2 * 3.14 * self.__raio
class UI:
    @staticmethod
    def main():
        c = Circulo()
        c.raio = float(input("Digite o raio do círculo: "))
        print(c. c.calc_c())
UI.main()