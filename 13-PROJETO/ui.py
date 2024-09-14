from contato import Contato, Contatos
from views import view
class UI:
    @staticmethod
    def Menu():
        print("Digite 1 para inserir um contato;\nDigite 2 para listar os contatos;\nDigite 3 para atualizar algum contato;\nDigite 4 para excluir algum contato")
        return int(input("Insira um dígito: "))
    @staticmethod
    def Main():
        op = 0
        while op != 6:
            op = UI.Menu()
            if op == 1: UI.Inserir()
            if op == 2: UI.Listar()
            if op == 3: UI.Atualizar()
            if op == 4: UI.Excluir()
        print("Você terminou a operação.")
    @staticmethod
    def Listar():
        print(Contatos.listar())
    @staticmethod
    def Inserir():
        Id = int(input("Insira o ID da avaliação: "))
        Disciplina = input("Insira o nome da disciplina: ")
        Local = input("Insira o local da avaliação: ")
        Data = input("Insira a data da avaliação: ")
        a = Contato(Id, Disciplina, Local, Data)
        Contatos.inserir(a)
    @staticmethod
    def Atualizar():
        Id = int(input("Insira o ID da avaliação: "))
        print(Contatos.atualizar(Id))
    @staticmethod
    def Excluir():
        Id = int(input("Insira o ID da avaliação: "))
        print(Contatos.excluir(Id))
UI.Main()