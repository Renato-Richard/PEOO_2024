class Pais:
    def __init__(self):
        self.__nome = " "
        self.__população = 0
        self.__area = 0
    def set_nome(self, x):
        if self.__nome != "": self.__nome = x
        else: raise ValueError("nome inválido.") # não coloquei excessão, nome não pode ser vazio. 
    def set_população(self, x):
        if self.__população > 0: self.__população = x
        else: raise ValueError("Número inválido.")
    def set_area(self, x):
        if self.__area < 0: self.__area = x
        else: raise ValueError("Número inválido")
    def get_nome(self):
        return self.__nome
    def get_população(self):
        return self.__população
    def get_area(self):
        return self.__area
    def densidade(self):
        return self.__população / self.__area
class UI:
    @staticmethod
    def menu():
        entrada = int(input("1 - Calcular, 2 - Fim: "))
        return entrada
    def main():
        while UI.menu() == 1: # coloquei while entrada == 1:
            UI.calculo()
    def calculo():
        P = Pais()
        nome = input("Digite o nome do país: ")
        população = int(input("Digite o número de habitantes: "))
        area = int(input("Digite a area do país: "))
        print(f"A densidade do país {P.set_nome(nome)}, com população de {P.set_população(população)} e área de {P.set_area(area)} era de: {P.densidade()}") # não coloquei P.densidade() nem print()
UI.main()