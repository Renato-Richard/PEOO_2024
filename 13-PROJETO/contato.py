import json
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
            c.d = obj.d
            c.l = obj.l
            c.dt = obj.dt
        cls.salvar()
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_Id(obj.id)
        if c != None: 
            cls.contatos.remove(c)
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
                    c = Contato(obj["id"], obj["nome"], obj["telefone"])
                cls.__compromissos.append(c)
        except FileNotFoundError:
            pass