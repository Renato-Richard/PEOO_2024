class Grupo:
    def __init__(self, id: int, nome: str):
        self.__id = 0
        self.__nome = ""
        if id > 0: self.__id = 0
        else: raise ValueError("ID inválido.")
        if nome != "": self.__nome = nome
        else: raise ValueError("Nome do Grupo inválido.")
    def __str__(self):
        return f"{self.__id} -  {self.__nome}"