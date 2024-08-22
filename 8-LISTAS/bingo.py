import random
class Bingo:
    def __init__(self):
        self.__numBolas = 0
        self.__bolasSort = []
    def iniciar(self, numBolas: int):
        if numBolas > 0: self.__numBolas = numBolas
        else: raise ValueError("Valor inválido.")
        self.__bolasSort.clear()
    def proximo(self):
        if len(self.__bolasSort) == self.__numBolas: return "Fim do jogo."
        sorteador = random.randint(1, self.__numBolas)
        while sorteador in self.__bolasSort: sorteador = random.randint(1, self.__numBolas)
        self.__bolasSort.append(sorteador)
        return sorteador
    def sorteados(self):
        return sorted(self.__bolasSort)
    def __str__(self):
        return f"Foram sorteadas {len(self.__bolasSort)} bolas de um toal de {self.__numBolas}."
class UI:
    @staticmethod
    def menu():
        print("SEJA BEM-VINDO(A) AO BINGO DE INFOWEB:\n", "Vamos começar!", "Escolha uma opção a seguir para continuar o jogo:\n", "Digite 1 para iniciar o jogo.\nDigite 2 para sortear um número.\nDigite 3 para conferir os números sorteados.\nDigite 4 para conferir a quantidade de números sorteados das bolas existentes.\nDigite 0 para terminar de jogar.", sep="\n")
        return int(input())
    @staticmethod
    def main():
        b = Bingo()
        opção = 5
        while opção != 0:
            opção = UI.menu()
            if opção == 1: UI.iniciarUI(b)
            if opção == 2: UI.proximoUI(b)
            if opção == 3: UI.sorteadosUI(b)
            if opção == 4: UI.info(b)
        print("Você terminou o jogo.")
    @staticmethod
    def iniciarUI(b):
        print("Quantas bolas terá o jogo? (informe um número. Ex.: 10:)")
        numBolas = int(input())
        b.iniciar(numBolas)
    @staticmethod
    def proximoUI(b):
        print(b.proximo())
    @staticmethod
    def sorteadosUI(b):
        print(b.sorteados())
    @staticmethod
    def info(b):
        print(b)
UI.main()