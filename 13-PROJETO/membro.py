import json
class Membro:
    def __init__(self, id: int, idGrupo, idContato, nome, usuario: str):
        self.id = id
        self.idGrupo = idGrupo
        self.idContato = idContato
        self.nome = ""
        self.usuario = ""
        if nome != "": self.nome = nome
        else: raise ValueError("Nome do Membro inválido.")
        if usuario != "": self.usuario = usuario
        else: raise ValueError("Nome de Usuário inválido.")
    def __str__(self):
        return f"{self.id} - {self.idGrupo} - {self.idContato} - {self.nome} - {self.usuario}"
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
            c.nome = obj.nome
            c.usuario = obj.usuario
        cls.salvar()
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_Id(obj.id)
        if c != None: 
            cls.membros.remove(c)
        cls.salvar()
    @classmethod
    def salvar(cls):  
        with open("13-PROJETO\membros.json", mode = "w") as arquivo:
            json.dump(cls.membros, arquivo, default = vars) 
    @classmethod
    def abrir(cls):
        cls.membros = []
        try: 
            with open("13-PROJETO\membros.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    m = Membro(obj["id"], obj["idGrupo"], obj["idContato"], obj["nome"], obj["usuario"])
                cls.membros.append(m)
        except FileNotFoundError:
            pass