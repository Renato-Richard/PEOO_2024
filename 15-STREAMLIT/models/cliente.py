import json
class Cliente:
  def __init__(self, id: int, nome: str, email: str, fone: str, senha: str):
    self.id = 0
    self.nome = nome
    self.email = email
    self.fone = fone
    self.senha = senha
    if id > 0: self.__id = id
    else: raise ValueError("ID inválido")
    if nome != "": self.__nome = nome
    else: raise ValueError("Nome inválido")
    if email != "": self.__email = email
    else: raise ValueError("E-mail inválido")
    if fone != "": self.__fone = fone
    else: raise ValueError("Número de telefone inválido")
    if senha != "": self.__senha = senha
    else: raise ValueError("Senha inválida")
  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__senha}"
class Clientes:
  objetos = []
  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for c in cls.objetos:
      if c.id > m: m = c.id
    obj.id = m + 1  
    emails = set()
    for d in cls.objetos:
        if d.email in emails:
            raise ValueError("Este e-mail já existe")
        emails.add(d.email)
        cls.objetos.append(d)
    cls.objetos.append(obj)
    cls.salvar()
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.id == id: return c
    return None 
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
       c.nome = obj.nome
       c.email = obj.email
       c.fone = obj.fone
    cls.salvar()   
  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None: 
      cls.objetos.remove(c)
      cls.salvar()   
  @classmethod
  def salvar(cls):  
    with open("clientes.json", mode = "w") as arquivo:
        json.dump(cls.objetos, arquivo, default = vars) 
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try: 
      with open("clientes.json", mode = "r") as arquivo:
        texto = json.load(arquivo)
        for obj in texto:
          c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass