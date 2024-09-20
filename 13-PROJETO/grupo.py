import json
class Grupo:
    def __init__(self, id: int, nome: str, descricao: str, categoria: str):
        self.id = id
        self.nome = ""
        self.descricao = ""
        self.categoria = ""
        if nome != "": self.nome = nome
        else: raise ValueError("Nome do Grupo inválido.")
        if descricao != "": self.descricao = descricao
        else: raise ValueError("Descrição inválida.")
        if categoria != "": self.categoria = categoria
        else: raise ValueError("Categoria inválida.")
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.descricao} - {self.categoria}"
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
            c.descricao = obj.descricao
            c.categoria = obj.categoria
        cls.salvar()
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_Id(obj.id)
        if c != None: 
            cls.grupos.remove(c)
        cls.salvar()
    @classmethod
    def salvar(cls):  
        with open("13-PROJETO\grupos.json", mode = "w") as arquivo:
            json.dump(cls.grupos, arquivo, default = vars) 
    @classmethod
    def abrir(cls):
        cls.grupos = []
        try: 
            with open("13-PROJETO\grupos.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    c = Grupo(obj["id"], obj["nome"], obj["descricao"], obj["categoria"])
            cls.grupos.append(c)
        except FileNotFoundError:
            pass