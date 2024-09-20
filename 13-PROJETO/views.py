from contato import Contato, Contatos
from membro import Membro, Membros
from grupo import Grupo, Grupos
class View:
    @staticmethod
    def inserirContato(nome: str, telefone: str):
        c = Contato(0, nome, telefone)
        Contatos.inserir(c)
    @staticmethod
    def atualizarContato(id: int, nome: str, telefone: str):
        c = Contato(id, nome, telefone)
        Contatos.atualizar(c)
    @staticmethod
    def excluirContato(id: int):
        c = Contato(id, 0, 0)
        Contatos.excluir(c)
    @staticmethod
    def inserirGrupo(nome: str, descricao: str, categoria: str):
        g = Grupo(0, nome, descricao, categoria)
        Grupos.inserir(g)
    @staticmethod
    def atualizarGrupo(id: int, nome: str, descricao: str, categoria: str):
        g = Grupo(id, nome, descricao, categoria)
        Grupos.atualizar(g)
    @staticmethod
    def excluirGrupo(id: int):
        g = Grupo(id, 0, 0, 0)
        Grupos.excluir(g)
    @staticmethod
    def inserirMembro(idGrupo: list, idContato: int, nome: str, usuario: str):
        m = Membro(0, idGrupo, idContato, nome, usuario)
        Membros.inserir(m)
    @staticmethod
    def atualizarMembro(id: int, nome: str, usuario: str):
        m = Membro(id, 0, 0, nome, usuario)
        Membros.atualizar(m)
    @staticmethod
    def excluirMembro(id: int):
        m = Membro(id, 0, 0, 0, 0)
        Membros.excluir(m)