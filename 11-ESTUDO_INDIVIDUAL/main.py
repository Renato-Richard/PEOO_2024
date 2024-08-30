import json
class Paciente:
    def __init__(self, id: str, n: str, f: str, nc):
        self.__id = 0
        self.__nome = ""
        self.__fone = ""
        self.__nascimento = nc
        if id > 0: self.__id = id
        else: raise ValueError("ID Inválido.")
        if n != "": self.__nome = n
        else: raise ValueError("Nome inválido.")
        if f != "": self.__fone = f
        else: raise ValueError("Telefone inválido.")
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__nome} - {self.__fone} - {self.__nascimento}"
class Pacientes:
  pacientes = []  # atributo estático
  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0                     # cálculo do maior id utilizado - começa com 0
    for c in cls.objetos:     # percorre a lista de clientes - c é cada cliente
      if c.id > m: m = c.id   # compara o id de c com m (maior)
    obj.id = m + 1  
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
      #c.set_nome( obj.get_nome() )
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
    with open("clientes.json", mode = "w") as arquivo:   # write
      json.dump(cls.objetos, arquivo, default = vars) 
  @classmethod
  def abrir(cls):
    cls.objetos = []
    # try: 
    #   with open("clientes.json", mode = "r") as arquivo:   # read
        # texto = json.load(arquivo)
        # for obj in texto:
        #   c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])                     # dicionário
        #   cls.objetos.append(c)
    # except FileNotFoundError:
    #   pass
class Pacientes:
    pacientes = []
    @classmethod
    def Inserir(cls):
        pass
    def Listar(cls):
        pass
    def Listar_id(cls):
        pass
    def Inserir(cls):
        pass