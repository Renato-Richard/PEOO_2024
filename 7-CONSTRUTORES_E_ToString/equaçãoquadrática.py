import math
class EquaçãoQuadrática:
    def __init__(self):
        self.__a = 0.0
        self.__b = 0.0
        self.__c = 0.0
    def setA(self, a):
        self.__a = a
    def setB(self, b):
        self.__b = b
    def setC(self, c):
        self.__c = c
    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c
    def calcDelta(self):
        return (self.__b ** 2) - (4 * self.__a * self.__c)
    def TemRaizesReais(self):
        return self.calcDelta() >= 0
    def Raiz1(self):
        if self.TemRaizesReais():
            return (-self.__b + math.sqrt(self.calcDelta())) / (2 * self.__a)
        else: return "Impossivel calcular."
    def Raiz2(self):
        if self.TemRaizesReais():
            return (-self.__b - math.sqrt(self.calcDelta())) / (2 * self.__a)
        else: return "Impossível calcular."
class UI:
    @staticmethod
    def menu(eq):
        print("SEJA BEM-VINDO(A) A EQUAÇÃO POLINOMIAL DO SEGUNDO GRAU\nA Equação Quadrática é definido por (ax² + bx + c)")
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        c = float(input("Digite o valor de C: "))
        eq.setA(a), eq.setB(b), eq.setC(c)
    @staticmethod
    def main():
        eq = EquaçãoQuadrática()
        UI.menu(eq)
        if eq.calcDelta() == 0:
            print(f"x = {eq.Raiz1()}")
        else:
            print(f"x1 = {eq.Raiz1()}\nx2 = {eq.Raiz2()}")
UI.main()