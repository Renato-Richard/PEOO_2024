from datetime import datetime
class Paciente:
    def __init__(self, n: str, c: str, t: str, nasc):
        self.__nome = ""
        self.__cpf = ""
        self.__telefone = ""
        self.__nascimento = nasc
        if self.__nome != "": self.__nome = n
        else: raise ValueError("O nome está vazio!")
        if self.__cpf != "": self.__cpf = c
        else: raise ValueError("O CPF está vazio!")
        if self.__telefone != "": self.__telefone = t
        else: raise ValueError("O número de telefone está vazio!")
    def idade(self, passado):
        presente = datetime.now()
        nascimento = datetime.strptime(passado, "%d/%m/%Y")
        anos = (presente - nascimento).days // 365
        meses = ((presente - nascimento).days % 365) // 30
        return f"A idade do paciente é {anos} anos e {meses} meses"
class UI:
    @staticmethod
    def menu():
        print("Digite os dados do paciente:\n1: Dados\n2: Informações")
        return int(input())
    @staticmethod
    def main():
        p = Paciente()
        op = -1
        while op != 0:
            op = UI.menu()
            if op == 1: UI.dados()
            if op == 2: UI.info(p)
        print("Operação terminada.")
    @staticmethod
    def dados():
        nome = input("Informe o nome do paciente: ")
        cpf = input("Informe o seu CPF: ")
        telefone = input("Informe o seu telefone: ")
        nascimento = input("Infome a sua data de nascimento: ")
        p = Paciente(nome, cpf, telefone, nascimento)
        print(p.idade(nascimento))
        return p
    @staticmethod
    def info(p):
        print(p)
UI.main()