class Jogador:
    def __init__(self, nome: str, camisa: int, gols: int):
        self.__nome = ""
        self.__camisa = camisa
        self.__gols = gols
        if self.__nome != "": self.__nome = nome
        else: raise ValueError("Nome inválido.")
        if self.__camisa > 0: self.__camisa = camisa
        else: raise ValueError("Número inválido.")
        if self.__gols > 0: self.__gols = gols
        else: raise ValueError("Número inválido.")
    def __str__(self):
        return f"{self.__nome} - {self.__camisa} - {self.__gols}"