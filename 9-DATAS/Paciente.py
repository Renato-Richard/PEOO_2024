from datetime import datetime
class Paciente:
    def __init__(self):
        self.__nome = ""
        self.__cpf = ""
        self.__telefone = ""
        self.__nascimento = ""
    def paciente(self, n: str, c: str, t: str, nasc: datetime):
        if self.__nome != "": self.__nome = n
        else: raise ValueError("O nome está vazio!")
        if self.__cpf != "": self.__cpf = c
        else: raise ValueError("O CPF está vazio!")
        if self.__telefone != "": self.__telefone = t
        else: raise ValueError("O número de telefone está vazio!")
        if self.__nascimento != "": self.__nascimento = nasc
        else: raise ValueError("A data de nascimento está vazia!")
    def idade(self, f):
        hoje = datetime.now()
class UI:
    @staticmethod
    def menu():
        pass
    @staticmethod
    def main():
        pass
    @staticmethod
    def metodo():
        pass