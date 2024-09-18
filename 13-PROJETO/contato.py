import json
class Contato:
    def __init__(self, id: int, nome: str, telefone: str):
        self.id = id
        self.nome = ""
        self.telefone = ""
        if nome != "": self.nome = nome
        else: raise ValueError("Nome inválido.")
        if telefone != "": self.telefone = telefone
        else: raise ValueError("Telefone inválido.")
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.telefone}"
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
        with open("13-PROJETO\contatos.json", mode = "w") as arquivo:
            json.dump(cls.contatos, arquivo, default = vars) 
    @classmethod
    def abrir(cls):
        cls.contatos = []
        try: 
            with open("13-PROJETO\contatos.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    c = Contato(obj["id"], obj["nome"], obj["telefone"])
                cls.contatos.append(c)
        except FileNotFoundError:
            pass