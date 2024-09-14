import json
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
class Grupos:
    grupos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.grupos:
            if c.id > m: m = c.id
        obj.id = m + 1  
        cls.grupos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.grupos
    @classmethod
    def listar_Id(cls, id):
        cls.abrir()
        for c in cls.grupos:
            if c.id == id: return c
        return None
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_Id(obj.id)
        if c != None:
            c.id = obj.id
            c.nome = obj.nome
        cls.salvar()
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_Id(obj.id)
        if c != None: 
            cls.grupos.remove(c)
        cls.salvar()
    @classmethod
    def salvar(cls):  
        with open("membros.json", mode = "w") as arquivo:
            json.dump(cls.contatos, arquivo, default = vars) 
    @classmethod
    def abrir(cls):
        cls.grupos = []
        try: 
            with open("membros.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    c = Grupo(obj["id"], obj["nome"])
            cls.grupos.append(c)
        except FileNotFoundError:
            pass