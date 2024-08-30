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
    def idade(self, passado):
        presente = datetime.now()
        nascimento = datetime.strptime(passado, "%d/%m/%Y")
        anos = (presente - nascimento).days // 365
        meses = ((presente - nascimento).days % 365) // 30
        return f"A idade do paciente é {anos} anos e {meses} meses"
class UI:
    @staticmethod
    def menu():
        print("Digite os dados do paciente:\n1: Nome\n2: CPF\n3: Telefone\n4: Nascimento")
        return int(input())
    @staticmethod
    def main():
        input("Informe o nome do paciente: ")
        input("Informe o seu CPF: ")
        input("Informe o seu telefone: ")
        passado = input("Infome a sua data de nascimento: ")
        p = Paciente()
        print(p.idade(passado))
UI.main()