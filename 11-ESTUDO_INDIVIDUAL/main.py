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