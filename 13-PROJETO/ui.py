# from membro import Membro, Membros
# from grupo import Grupo, Grupos
from contato import Contato, Contatos
from views import View
class UI:
    @staticmethod
    def menuContato():
        print("Digite 1 para inserir um contato;\nDigite 2 para listar os contatos;\nDigite 3 para atualizar algum contato;\nDigite 4 para excluir algum contato;\nDigite 0 para acessar o Sahto Mensenger!")
        return int(input("Insira um dígito: "))
    @staticmethod
    def inserirContato():
        nome = input("Insira o seu nome: ")
        telefone = input("Insira o seu telefone: ")
        View.inserir(nome, telefone)
    @staticmethod
    def listarContato():
        for c in Contatos.listar():
            print(c)
    @staticmethod
    def atualizarContato():
        id = int(input("Insira o ID do contato: "))
        nome = input("Insira o seu novo nome: ")
        telefone = input("Insira o seu novo telefone: ")
        View.atualizar(id, nome, telefone)
    @staticmethod
    def excluirContato():
        id = int(input("Insira o ID do contato: "))
        View.excluir(id)
    @staticmethod
    # def menuGrupo():
    #     print("Digite 1 para criar um grupo;\nDigite 2 para listar os grupos existentes;\nDigite 3 para atualizar os dados de um grupo;\nDigite 4 para excluir algum grupo.")
    #     return int(input("Insira um dígito: "))
    # @staticmethod
    # def inserirGrupo():
    #     nome = input("Insira o nome do grupo: ")
    #     descricao = input("Insira uma breve descrição: ")
    #     categoria = input("Informe uma categoria para o grupo: ")
    #     g = Grupo(nome, descricao, categoria)
    #     Grupos.inserir(g)
    # @staticmethod
    # def listarGrupo():
    #     for g in Grupos.listar():
    #         print(g)
    # @staticmethod
    # def atualizarGrupo():
    #     pass
    # @staticmethod
    # def excluirGrupo():
    #     pass
    @staticmethod
    def main():
        print("Olá! Somos o Sahto Mensenger!\n\nInsira contatos à sua lista:\n\n")
        op = 6
        while op != 777:
            op = UI.menuContato()
            if op == 1: UI.inserirContato()
            if op == 2: UI.listarContato()
            if op == 3: UI.atualizarContato()
            if op == 4: UI.excluirContato()
            if op == 0:
                if Contatos.listar() == []:
                    print("\nVocê precisa adicionar algum contato!\n")
                else:
                    print("\nPronto! Contatos criados com sucesso!\n\nVamos criar um grupo para interagir com os seus amigos!")
                    break
        # op = 6
        # while op != 777:
        #     op = UI.menuGrupo()
        #     if op == 1: UI.inserirGrupo()
        #     if op == 2: UI.listarGrupo()
        #     if op == 3: UI.atualizarGrupo()
        #     if op == 4: UI.excluirGrupo()
UI.main()