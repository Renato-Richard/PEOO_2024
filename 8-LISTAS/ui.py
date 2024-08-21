# from playlist import Playlist
# from música import Musica
# class UI:
#     @staticmethod
#     def menu():
#         print("1 - Nova playlist, 2 - Inserir música, 3 - Listar músicas, 4 - Info, 5 - Fim")
#         return int(input("Escolha uma opção: "))
#     @staticmethod
#     def main():
#         print("Bem-vindo(a) ao IF Música")
#         operação = 0
#         while operação != 5:
#             operação = UI.menu()
#             if operação == 1: p = UI.nova_playlist()
#             if operação == 2: UI.inserir_musica(p)
#             if operação == 3: UI.listar_musica(p)
#             if operação == 4: UI.info(p)
#         print("Bye")
#     @staticmethod
#     def nova_playlist():
#         nome = input("Informe o título da música")
#         descrição = input("Infome um descrição para a playlist")
#         p = Playlist(nome, descrição)
#         return p
#     @staticmethod
#     def inserir_musica(p):
        