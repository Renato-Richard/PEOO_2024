import math
class EquaçãoQuadrática:
    def __init__(self, a: float, b: float, c: float):
        self.__a = a
        self.__b = b
        self.__c = c
    def setA(self, x):
        if x > 0: self.__b = x
        else: raise ValueError("Número inválido.")
    def setB(self, x):
        if x > 0: self.__h = x
        else: raise ValueError("Número inválido.")
    def setC(self, x):
        if x > 0: self.__h = x
        else: raise ValueError("Número inválido.")
    def getA(self):
        return self.__b
    def getB(self):
        return self.__h
    def getC(self):
        return self.__h
    def calcDelta(self):
        return self.__b ** 2 * 4 * self.__a * self.__c
    def TemRaizesReais(self):
        if EquaçãoQuadrática.calcDelta() < 0:
            return "Impossivel calcular." 
    def Raiz1(self):
        return -self.__b + math.sqrt(EquaçãoQuadrática.calcDelta()) / 2 * self.__a
    def Raiz2(self):
        return -self.__b - math.sqrt(EquaçãoQuadrática.calcDelta()) / 2 * self.__a