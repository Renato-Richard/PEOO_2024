class Frete:
    def __init__(self, d: float, p: float):
        self.__d = d
        self.__p = p
    def set_distancia(self, x):
        if x > 0: self.__d = x
        else: raise ValueError("Número inválido.")
    def setPeso(self, x):
        if x > 0: self.__p = x
        else: raise ValueError("Número inválido.")
    def getDistancia(self):
        return self.__d
    def getPeso(self):
        return self.__p
    def calcFrete(self):
        return self.__d * self.__p
    def __str__(self):
        return f"distancia = {self.__d} - peso = {self.__p}"