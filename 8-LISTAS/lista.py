import random
class Bingo:
    def __init__(self, numBolas: int):
        self.__numBolas = numBolas
    def Iniciar(self, numBolas: int):
        self.__numBolas = 10
    def Proximo(self):
        return random.randint(1, self.__numBolas)
    def Sorteados(self):
        return [Bingo.Proximo()]
# class UI:
#     @staticmethod
#     def main():
#         numBolas = int(input())