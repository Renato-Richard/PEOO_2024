from contato import Contato, Contatos
from membro import Membro, Membros
from grupo import Grupo, Grupos
from views import View
class UI:
    @staticmethod
    def menuContato():
        print("Digite 1 para inserir um contato;\nDigite 2 para listar os contatos;\nDigite 3 para atualizar algum contato;\nDigite 4 para excluir algum contato;\nDigite 0 para terminar.")
        return int(input("Insira um dígito: "))
    @staticmethod
    def mainContato():
        print("Insira contatos à sua lista:\n")
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
                    print("\nPronto! Contato(s) criado(s) com sucesso!\n\nVamos criar um grupo para interagir com os seus amigos!\n")
                    break
    @staticmethod
    def inserirContato():
        nome = input("Insira o seu nome: ")
        telefone = input("Insira o seu telefone: ")
        View.inserirContato(nome, telefone)
    @staticmethod
    def listarContato():
        for c in Contatos.listar():
            print(c)
    @staticmethod
    def atualizarContato():
        id = int(input("Insira o ID do contato: "))
        nome = input("Insira o novo nome: ")
        telefone = input("Insira o novo telefone: ")
        View.atualizarContato(id, nome, telefone)
    @staticmethod
    def excluirContato():
        id = int(input("Insira o ID do contato: "))
        View.excluirContato(id)
    @staticmethod
    def menuGrupo():
        print("Digite 1 para criar um grupo;\nDigite 2 para listar os grupos existentes;\nDigite 3 para atualizar os dados de um grupo;\nDigite 4 para excluir algum grupo;\nDigite 0 para terminar.")
        return int(input("Insira um dígito: "))
    @staticmethod
    def mainGrupo():
        print("Crie grupos:\n")
        op = 6
        while op != 777:
            op = UI.menuGrupo()
            if op == 1: UI.inserirGrupo()
            if op == 2: UI.listarGrupo()
            if op == 3: UI.atualizarGrupo()
            if op == 4: UI.excluirGrupo()
            if op == 0:
                if Grupos.listar() == []:
                    print("\nVocê precisa adicionar algum grupo para interagir com seus amigos!\n")
                else:
                    print("\nPronto! Grupo(s) criado(s) com sucesso!\n\nVamos adicionar membros aos grupos.\n")
                    break
    @staticmethod
    def inserirGrupo():
        nome = input("Insira o nome do grupo: ")
        descricao = input("Insira uma breve descrição: ")
        categoria = input("Informe uma categoria para o grupo: ")
        View.inserirGrupo(nome, descricao, categoria)
    @staticmethod
    def listarGrupo():
        for g in Grupos.listar():
            print(g)
    @staticmethod
    def atualizarGrupo():
        id = int(input("Insira o ID do grupo: "))
        nome = input("Insira o novo nome: ")
        descricao = input("Insira uma nova descrição: ")
        categoria = input("Insira uma nova categoria: ")
        View.atualizarGrupo(id, nome, descricao, categoria)
    @staticmethod
    def excluirGrupo():
        id = int(input("Insira o ID do grupo: "))
        View.excluirGrupo(id)
    @staticmethod
    def menuMembro():
        print("Digite 1 para criar um membro;\nDigite 2 para listar os membros;\nDigite 3 para atualizar os dados de um membro;\nDigite 4 para excluir algum membro;\nDigite 0 para terminar.")
        return int(input("Insira um dígito: "))
    @staticmethod
    def mainMembro():
        print("Crie membros:\n")
        op = 6
        while op != 777:
            op = UI.menuMembro()
            if op == 1: UI.inserirMembro()
            if op == 2: UI.listarMembro()
            if op == 3: UI.atualizarMembro()
            if op == 4: UI.excluirMembro()
            if op == 0:
                if Membros.listar() == []:
                    print("\nVocê precisa adicionar algum membro!\n")
                else:
                    print("\nPronto! Membro(s) criado(s) com sucesso!\n\n")
                    break
    @staticmethod
    def inserirMembro():
        idGrupo = int(input("Insira o id do grupo: "))
        idContato = int(input("Qual o id do contato? "))
        nome = input("Insira o nome do membro: ")
        usuario = input("Insira um nome de usuário: ")
        View.inserirMembro(idGrupo, idContato, nome, usuario)
    @staticmethod
    def listarMembro():
        for m in Membros.listar():
            print(m)
    @staticmethod
    def atualizarMembro():
        id = int(input("Insira o ID do membro: "))
        nome = input("Insira o novo nome: ")
        usuario = input("Insira um novo nome de usuário: ")
        View.atualizarMembro(id, nome, usuario)
    @staticmethod
    def excluirMembro():
        id = int(input("Insira o ID do membro: "))
        View.excluirMembro(id)
    @staticmethod
    def menu():
        print("Olá! Somos o Sahto Mensenger!\n\nAdicione contatos à sua lista, crie grupos e gerencie os membros.\n\nDigite 1 para gerenciar sua lista de contatos;\nDigite 2 para criar grupos;\nDigite 3 para gerenciar membros.\n\n")
        return int(input("Insira um dígito: "))
    @staticmethod
    def main():
        opcao = 8
        while opcao != 999:
            opcao = UI.menu()
            if opcao == 1: UI.mainContato()
            if opcao == 2: UI.mainGrupo()
            if opcao == 3: UI.mainMembro()
UI.main()