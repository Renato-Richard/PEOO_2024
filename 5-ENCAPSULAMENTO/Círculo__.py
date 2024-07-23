class Circulo:
    def __init__ (self):
        self.__raio = 0
    def set_raio(self, v):
        if v > 0: self.__raio = v
        else: raise ValueError("O raio deve ser um número positivo")
    def get_raio(self):
        return self.__raio
    def calc_area(self):
        return 3.14 * self.__raio ** 2 
    def calc_cirucunferencia(self):
        return 2 * 3.14 * self.__raio
class UI:
    @staticmethod
    def main():
        c = Circulo()
        raio = float(input("Digite o raio do círculo: "))
        c.set_raio(raio)
        print(f"Área: {c.calc_area():.2f}")
        print(f"Circunferência: {c.calc_cirucunferencia():.2f}")
UI.main()