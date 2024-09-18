import json
class Membro:
    def __init__(self, id: int, grupo,):
        self.id = id
        self.grupo = grupo
    def __str__(self):
        return f"{self.id} - {self.grupo}"
class Membros:
    membros = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.membros:
            if c.id > m: m = c.id
        obj.id = m + 1
        cls.membros.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.membros
    @classmethod
    def listar_Id(cls, id):
        cls.abrir()
        for c in cls.membros:
            if c.id == id: return c
        return None
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_Id(obj.id)
        if c != None:
            c.id = obj.id
            c.grupo = obj.grupo
        cls.salvar()
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_Id(obj.id)
        if c != None: 
            cls.membros.remove(c)
        cls.salvar()
    @classmethod
    def salvar(cls):  
        with open("./membros.json", mode = "w") as arquivo:
            json.dump(cls.membros, arquivo, default = vars) 
    @classmethod
    def abrir(cls):
        cls.membros = []
        try: 
            with open("membros.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    m = Membro(obj["id"], obj["grupo"])
                cls.membros.append(m)
        except FileNotFoundError:
            pass