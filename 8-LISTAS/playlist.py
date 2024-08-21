class Playlist:
    def __init__(self, nome, descrição):
        self.__nome = nome
        self.__descrição = descrição
        if nome == "": raise ValueError("Nome da playlist inválida.")
    def Inserir(self, m):
        self.__musicas.append(m)
    def Listar(self):
        return self.__musicas[:]
    def __str__(self):
        return f"Playlist {self.__nome} - {self.__descrição} tem {len(self.__musicas)} músicas."