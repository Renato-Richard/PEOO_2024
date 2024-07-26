import math
class Retangulo:
    def __init__(self, b: float, h: float):
        self.__b = b
        self.__h = h
    def setBase(self, x):
        if x > 0: self.__b = x
        else: raise ValueError("Número inválido.")
    def setAltura(self, x):
        if x > 0: self.__h = x
        else: raise ValueError("Número inválido.")
    def getBase(self):
        return self.__b
    def getAltura(self):
        return self.__h
    def calcArea(self):
        return self.__b * self.__h
    def calcDiagonal(self):
        return math.sqrt(self.__b ** 2 + self.__h ** 2)
    def __str__(self):
        return f"Base = {self.__b} - Altura = {self.__h}"