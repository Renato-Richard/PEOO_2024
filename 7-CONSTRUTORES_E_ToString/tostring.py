class Pais:
    def __init__(self, nome, população: int, area: int):
        self.__nome = nome
        self.__população = população
        self.__area = area
    def set_nome(self, x):
        if x != "": self.__nome = x
        else: raise ValueError("Nome inválido.")
    def set_população(self, x):
        if x > 0: self.__população = x
        else: raise ValueError("Número inválido.")
    def set_area(self, x):
        if x > 0: self.__area = x
        else: raise ValueError("Número inválido")
    def get_nome(self):
        return self.__nome
    def get_população(self):
        return self.__população
    def get_area(self):
        return self.__area
    def densidade(self):
        return self.__população / self.__area
    def __str__(self):
        return f"Nome = {self.__nome} - População = {self.__população} - Area = {self.__area}"
class UI:
    @staticmethod
    def menu():
        entrada = int(input("1 - Calcular, 2 - Fim: "))
        return entrada
    def main():
        while UI.menu() == 1:
            UI.calculo()
    def calculo():
        nome = input("Digite o nome do país: ")
        população = int(input("Digite o número de habitantes: "))
        area = int(input("Digite a area do país: "))
        P = Pais(nome, população, area)
        print(P)
        print(f"A densidade demográfica é de: {P.densidade():.2f}")
UI.main()