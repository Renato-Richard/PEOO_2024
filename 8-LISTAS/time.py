from jogador import Jogador
class Time:
    def __init__(self, nome: str, estado: str, jogadores: list):
        self.__nome = nome
        self.__estado = estado
        self.__jogadores = jogadores
        if self.__nome != "" : self.__nome = nome
        else: raise ValueError("Nome inválido.")
        if self.__estado != "" : self.__estado = estado
        else: raise ValueError("Nome inválido.")
    def Inserir(self, j):
        self.__jogadores.append(j)
    def Listar(self):
        pass
    def Artilheiro(self):
        pass
    def __str__(self):
        return f"{self.__nome} - {self.__estado} - {self.__jogadores}"
class UI:
    @staticmethod
    def menu_jogador():
        print("Adicione um novo jogador!")
        return int(input("Digite 1 para inserir o nome do jogador, digite 2 para informar o número de sua camisa, digite 3 para o informar o número de gols do jogador e digite 0 para terminar a adição do jogador."))
    @staticmethod
    def menu_time():
        print("Crie um novo time!")
        return int(input("Digite 1 para inserir o nome do time, digite 2 para informar o estado do time e digite 3 para terminar o seu time."))
    @staticmethod
    def main():
        while UI.menu_jogador() != 0:
            return UI.menu_jogador()
        while UI.menu_time() != 0:
            return UI.menu_time()
    @staticmethod
    def método():
        pass