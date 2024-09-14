import json
from views import View
class Contato:
    def __init__(self, id: int, nome: str, telefone: str):
        self.__id = 0
        self.__nome = ""
        self.__telefone = ""
        if id > 0: self.__id = id
        else: raise ValueError("ID inválido.")
        if nome != "": self.__nome = nome
        else: raise ValueError("Nome inválido.")
        if telefone != "": self.__telefone = telefone
        else: raise ValueError("Telefone inválido.")
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__telefone}"
class Contatos:
    contatos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.contatos:
            if c.id > m: m = c.id
        obj.id = m + 1  
        cls.contatos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.contatos
    @classmethod
    def listar_Id(cls, id):
        cls.abrir()
        for c in cls.contatos:
            if c.id == id: return c
        return None
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_Id(obj.id)
        if c != None:
            c.id = obj.id
            c.nome = obj.nome
            c.telefone = obj.telefone
        cls.salvar()
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_Id(obj.id)
        if c != None: 
            cls.contatos.remove(c)
        cls.salvar()
    @classmethod
    def salvar(cls):  
        with open("contatos.json", mode = "w") as arquivo:
            json.dump(cls.contatos, arquivo, default = vars) 
    @classmethod
    def abrir(cls):
        cls.contatos = []
        try: 
            with open("contatos.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    c = Contato(obj["id"], obj["nome"], obj["telefone"])
                cls.contatos.append(c)
        except FileNotFoundError:
            pass
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
    def Inserir(Id, Disciplina, Local, Data):
        Id = int(input("Insira o ID da avaliação: "))
        Disciplina = input("Insira o nome da disciplina: ")
        Local = input("Insira o local da avaliação: ")
        Data = input("Insira a data da avaliação: ")
    @staticmethod
    def Atualizar():
        Id = int(input("Insira o ID da avaliação: "))
        print(Contatos.atualizar(Id))
    @staticmethod
    def Excluir():
        Id = int(input("Insira o ID da avaliação: "))
        print(Contatos.excluir(Id))
UI.Main()
# class View:
#     @staticmethod
#     def inserir_ui():
#         a = Contato(UI.Inserir(Id, Disciplina, Local, Data))
#         Contatos.inserir(a)