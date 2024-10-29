import json
from datetime import datetime
class Horario:
    def __init__(self, id: int, data: str, confirmado: bool, idCliente: 0, idServiço: int):
        self.id = 0
        self.data = ""
        self.confirmado = confirmado
        self.idCliente = 0
        self.idServico = 0
        if id > 0: self.__id = id
        else: raise ValueError("ID inválido.")
        if data != "": self.data = data
        else: raise ValueError("Data inválida.")
        if idCliente > 0: self.idCliente = idCliente
        else: raise ValueError("ID Cliente inválida.")
        if idServiço > 0: self.idServico = idServiço
        else: raise ValueError("ID Serviço inválida.")
    def __str__(self):
        return f"{self.__id} {self.data} {self.confirmado} {self.idCliente} {self.idServico}"
    class Horarios:
        objetos = []
        @classmethod
        def setObj(cls, objetos):
            cls.__objetos = objetos
        def getObj(cls):
            return cls.__objetos
        @classmethod
        def inserir(cls):
            pass
        @classmethod
        def listar(cls):
            pass
        @classmethod
        def listar_Id(cls):
            pass
        @classmethod
        def atualizar(cls):
            pass
        @classmethod
        def excluir(cls):
            pass
        @classmethod
        def abrir(cls):
            cls.__objetos = []
            try:
                with open("clientes.json", mode = "") as arquivo:
                    texto = json.load(arquivo)
                    for obj in texto:
                        h = Horario(obj["id"], obj["nome"], obj["email"], obj["fone"])
                        cls.__objetos.append(h)
            except FileNotFoundError:
                pass
        @classmethod
        def salvar(cls):
            with open("clientes.json", mode = "w") as arquivo:
                json.dump(cls.__objetos, arquivo, default = vars) 
            pass