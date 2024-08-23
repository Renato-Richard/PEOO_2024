import math
class Retangulo:
    def __init__(self):
        self.__b = 0.0
        self.__h = 0.0
    def setBase(self, b: float):
        if b > 0: self.__b = b
        else: raise ValueError("Número inválido.")
    def setAltura(self, h: float):
        if h > 0: self.__h = h
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
class UI:
    @staticmethod
    def menu():
        print("Digite 1 para realizar o cálculo da área.\nDigite 2 para realizar o cálculo da diagonal.\nDigite 3 para conferir as informações de base e altura escolhidas por você.\nDigite 0 para terminar de calcular.")
        return int(input())  
    @staticmethod
    def main():
        r = Retangulo()
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        r.setBase(base), r.setAltura(altura)
        menu = 1
        while menu != 0:
            menu = UI.menu()
            if menu == 1: UI.calcAreaUI(r)
            if menu == 2: UI.calcDiagonal(r)
            if menu == 3: UI.info(r)
        print("Você terminou o cálculo.")
    @staticmethod
    def calcAreaUI(r):
        print(f"Área: {r.calcArea():.2f}")
    @staticmethod
    def calcDiagonal(r):
        print(f"Diagonal: {r.calcDiagonal():.2f}")
    @staticmethod
    def info(r):
        print(r)
UI.main()