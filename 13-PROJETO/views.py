from contato import Contato, Contatos
class View:
    @staticmethod
    def inserir(nome: str, telefone: str):
        c = Contato(0, nome, telefone)
        Contatos.inserir(c)
    @staticmethod
    def atualizar(id: int, nome: str, telefone: str):
        c = Contato(id, nome, telefone)
        Contatos.atualizar(c)
    @staticmethod
    def excluir(id: int):
        c = Contato(id, 0, 0)
        Contatos.excluir(c)