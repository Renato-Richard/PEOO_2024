from contato import Contato, Contatos
from grupo import Grupo, Grupos
from membro import Membro, Membros
class View:
    @staticmethod
    def contato_inserir(id, nome, telefone):
        Contatos.inserir(id, nome, telefone)