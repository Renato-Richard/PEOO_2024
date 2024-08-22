class Frete:
    def __init__(self):
        self.__d = 0.0
        self.__p = 0.0
    def setDistancia(self, d):
        if d > 0: self.__d = d
        else: raise ValueError("Número inválido.")
    def setPeso(self, p):
        if p > 0: self.__p = p
        else: raise ValueError("Número inválido.")
    def getDistancia(self):
        return self.__d
    def getPeso(self):
        return self.__p
    def calcFrete(self):
        return self.__d * self.__p
    def __str__(self):
        return f"distancia = {self.__d} - peso = {self.__p}"
class UI:
    @staticmethod
    def menu():
        print("Digite 1 para realizar o cálculo do frete.\nDigite 2 para conferir as informações de distância e peso escolhidas por você.\nDigite 0 para terminar de calcular.")
        return int(input())
    @staticmethod
    def main():
        f = Frete()
        d = float(input("Digite o valor da distância: "))
        p = float(input("Digite o valor do peso: "))
        f.setDistancia(d), f.setPeso(p)
        op = 1
        while op != 0:
            op = UI.menu()
            if op == 1: UI.calcFreteUI(f)
            if op == 2: UI.info(f)
        print("Você terminou o cálculo")
    @staticmethod
    def calcFreteUI(f):
        print(f"Frete: {f.calcFrete()}")
    @staticmethod
    def info(f):
        print(f)
UI.main()
