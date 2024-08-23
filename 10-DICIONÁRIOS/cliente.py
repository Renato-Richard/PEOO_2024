# from datetime import datetime
# import json
# # Modelo de clientes
# class Cliente:
#   def __init__(self, id, nome, email, fone):
#     self.id = id
#     self.nome = nome
#     self.email = email
#     self.fone = fone
#   def __str__(self):
#     return f"{self.id} - {self.nome} - {self.email} - {self.fone}"
# # Modelo de Horário
# class Horario:
#     def __init__(self, id: int, data, confirmado: bool, idCliente: 0, idServiço: int):
#         self.__id = 0
#         self.__data = 0
#         self.__confirmado = False
#         self.__idCliente = 0
#         self.__idServico = 0
#         if id > 0: self.__id = id
#         else: raise ValueError("ID inválido.")
#         self.__data = data
#         self.__confirmado = confirmado
#         self.__idCliente = idCliente
#         self.__idServico = idServiço
#     def __str__(self):
#         return f"{self.__id} {self.__data} {self.__confirmado} {self.__idCliente} {self.__idServico}" # a ver
# class Servico:
#     def __init__(self, id: int, descricao: str, valor: int, duracao: int):
#         self.__id = 0
#         self.__descricao = ""
#         self.__valor = 0.0
#         self.__duracao = 0
#         if id > 0: self.__id = id
#         else: raise ValueError("ID inválido")
#         if descricao != "": self.__descricao = descricao
#         else: raise ValueError("Descrição vazia.")
#         if valor > 0: self.__valor = valor
#         else: raise ValueError("Valor inválido.")
#         if duracao > 0: self.__duracao = duracao
#         else: raise ValueError("Valor inválido.")
#     def __str__(self):
#         return f"{self.__id} {self.__descricao} {self.__valor} {self.__duracao}"
# # Persistência
# class Clientes:
#   objetos = []  # atributo estático
#   @classmethod
#   def inserir(cls, obj):
#     cls.abrir()
#     m = 0                     # cálculo do maior id utilizado - começa com 0
#     for c in cls.objetos:     # percorre a lista de clientes - c é cada cliente
#       if c.id > m: m = c.id   # compara o id de c com m (maior)
#     obj.id = m + 1  
#     cls.objetos.append(obj)
#     cls.salvar()
#   @classmethod
#   def listar(cls):
#     cls.abrir()
#     return cls.objetos
#   @classmethod
#   def listar_id(cls, id):
#     cls.abrir()
#     for c in cls.objetos:
#       if c.id == id: return c
#     return None 
#   @classmethod
#   def atualizar(cls, obj):
#     c = cls.listar_id(obj.id)
#     if c != None:
#        c.nome = obj.nome
#        c.email = obj.email
#        c.fone = obj.fone
#     cls.salvar()   
#   @classmethod
#   def excluir(cls, obj):
#     c = cls.listar_id(obj.id)
#     if c != None: 
#       cls.objetos.remove(c)
#       cls.salvar()   
#   @classmethod
#   def salvar(cls):  
#     with open("clientes.json", mode = "w") as arquivo:   # write
#         json.dump(cls.objetos, arquivo, default = vars) 
#   @classmethod
#   def abrir(cls):
#     cls.objetos = []
#     try: 
#       with open("clientes.json", mode = "r") as arquivo:   # read
#         texto = json.load(arquivo)
#         for obj in texto:
#           c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])                     # dicionário
#           cls.objetos.append(c)
#     except FileNotFoundError:
#       pass
# class Horarios:
#     __objetos = []
#     @classmethod
#     def setObj(cls, objetos):
#         cls.__objetos = objetos
#     def getObj(cls):
#         return cls.__objetos
#     @classmethod
#     def inserir(cls):
#         pass
#     @classmethod
#     def listar(cls):
#         pass
#     @classmethod
#     def listar_Id(cls):
#         pass
#     @classmethod
#     def atualizar(cls):
#         pass
#     @classmethod
#     def excluir(cls):
#         pass
#     @classmethod
#     def abrir(cls):
#         cls.__objetos = []
#         try:
#             with open("clientes.json", mode = "") as arquivo:
#                 texto = json.load(arquivo)
#                 for obj in texto:
#                     c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
#                     cls.__objetos.append(c)
#         except FileNotFoundError:
#             pass
#     @classmethod
#     def salvar(cls):
#         with open("clientes.json", mode = "w") as arquivo:   # write
#             json.dump(cls.__objetos, arquivo, default = vars) 
#         pass
# # Visão
# class UI:
#   @staticmethod
#   def menu():
#     print("1 - Inserir cliente, 2 - listar clientes, 3 - atualizar cliente, 4 - excluir cliente, 9 - fim")
#     return int(input("Informe uma opção: "))
#   @staticmethod
#   def main():
#     op = 0
#     while op != 9: 
#       op = UI.menu()
#       if op == 1: UI.cliente_inserir()
#       if op == 2: UI.cliente_listar()
#       if op == 3: UI.cliente_atualizar()
#       if op == 4: UI.cliente_excluir()
#   @staticmethod
#   def cliente_inserir():
#     #id = int(input("Informe o id: "))
#     nome = input("Informe o nome: ")
#     email = input("Informe o e-mail: ")
#     fone = input("Informe o fone: ")
#     c = Cliente(0, nome, email, fone)
#     Clientes.inserir(c)
#   @staticmethod
#   def cliente_listar():
#     for c in Clientes.listar():
#       print(c)
#   @staticmethod
#   def cliente_atualizar():
#     UI.cliente_listar()
#     id = int(input("Informe o id do cliente a ser atualizado: "))
#     nome = input("Informe o novo nome: ")
#     email = input("Informe o novo e-mail: ")
#     fone = input("Informe o novo fone: ")
#     c = Cliente(id, nome, email, fone)
#     Clientes.atualizar(c)
#   @staticmethod
#   def cliente_excluir():
#     UI.cliente_listar()
#     id = int(input("Informe o id do cliente a ser excluído: "))
#     c = Cliente(id, "", "", "")
#     Clientes.excluir(c)
#     def horario_listar(self):
#         pass
#     def horario_inserir(self):
#         pass
#     def horario_atualizar(self):
#         pass
#     def horario_excluir(self):
#         pass
#     def servico_listar(self):
#         pass
#     def servico_inserir(self):
#         pass
#     def servico_atualizar(self):
#         pass
#     def servico_excluir(self):
#         pass
# UI.main()    