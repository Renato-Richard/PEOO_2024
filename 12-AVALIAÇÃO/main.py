import json
from datetime import datetime
class Avaliacao:
    def __init__(self, id: int, d: str, l: str, dt):
        self.id = id
        self.disciplina = d
        self.local = l
        self.data = dt
    def __str__(self):
        return f"{self.id} - {self.disciplina} - {self.local} - {datetime.strptime(self.data, '%d/%m/%Y')}"
    def To_Json(self):
        dic = {}
        dic["id"] = self.id
        dic["d"] = self.disciplina
        dic["l"] = self.local
        dic["dt"] = self.data.strftime("%d/%m/%Y")
        return dic
class Avaliacoes:
    __compromissos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.__compromissos:
            if c.id > m: m = c.id
        obj.id = m + 1  
        cls.__compromissos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__compromissos
    @classmethod
    def listar_Id(cls, id):
        cls.abrir()
        for c in cls.__compromissos:
            if c.id == id: return c
        return None 
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_Id(obj.id)
        if c != None:
            c.d = obj.d
            c.l = obj.l
            c.dt = obj.dt
        cls.salvar()
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_Id(obj.id)
        if c != None: 
            cls.__compromissos.remove(c)
        cls.salvar()
    @classmethod
    def salvar(cls):  
        with open("avaliacao.json", mode = "w") as arquivo:
            json.dump(cls.__compromissos, arquivo, default = vars) 
    @classmethod
    def abrir(cls):
        cls.__compromissos = []
        try: 
            with open("avaliacao.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    a = Avaliacao(obj["id"], obj["disciplina"], obj["local"], obj["data"])
                cls.__compromissos.append(a)
        except FileNotFoundError:
            pass
    @classmethod
    def proximosDias(cls, dias: int):
        pass
class UI:
    @staticmethod
    def Main():
        op = 0
        while op != 6:
            op = UI.Menu()
            if op == 1: UI.Inserir()
            if op == 2: UI.Listar()
            if op == 3: UI.Atualizar()
            if op == 4: UI.Excluir()
            if op == 5: UI.ProximosDias()
        print("Você terminou a operação.")
    @staticmethod
    def Menu():
        print("Digite 1 para inserir uma avaliação;\nDigite 2 para listar as avaliações;\nDigite 3 para atualizar alguma avaliação;\nDigite 4 para excluir alguma avaliação;\nDigite 5 para conferir as avaliações dos próximos dias.")
        return int(input("Insira um dígito: "))
    @staticmethod
    def Listar():
        print(Avaliacoes.listar())
    @staticmethod
    def Inserir():
        Id = int(input("Insira o ID da avaliação: "))
        Disciplina = input("Insira o nome da disciplina: ")
        Local = input("Insira o local da avaliação: ")
        Data = input("Insira a data da avaliação: ")
        a = Avaliacao(Id, Disciplina, Local, Data)
        Avaliacoes.inserir(a)
    @staticmethod
    def Atualizar():
        Id = int(input("Insira o ID da avaliação: "))
        print(Avaliacoes.atualizar(Id))
    @staticmethod
    def Excluir():
        Id = int(input("Insira o ID da avaliação: "))
        print(Avaliacoes.excluir(Id))
    @staticmethod
    def ProximosDias():
        print(Avaliacoes.proximosDias())
UI.Main()