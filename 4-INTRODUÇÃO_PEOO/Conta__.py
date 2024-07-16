class Conta:
    def __init__(self):
        self.__titular = " "
        self.__nConta = " "
        self.__saldo = 0
    def set_titular_nConta(self, x, y):
        self.__titular = x
        self.__nConta = y
    def set_saldo(self, v):
        self.__saldo = v
    def get_titular_nConta(self):
        return self.__titular, self.__nConta
    def get_saldo(self):
        return self.__saldo
    def depósito(self, v):
        self.__saldo = self.__saldo + v
    def saque(self, v):
        self.__saldo = self.__saldo - v
class UI:
    @staticmethod
    def main():
        c = Conta()
        titular = input("Nome do titular: ")
        nConta = input("Número da conta: ")
        c.set_titular_nConta(titular, nConta)
        operação = int(input("Digite 1 para consultar o saldo, digite 2 para realizar o depósito, digite 3 para sacar ou digite 0 para terminar a operação: "))
        while operação != 0:
            if operação == 1:
                print(c.get_saldo())
            elif operação == 2:
                valor = float(input("Digite o valor do depósito: "))
                c.depósito(valor)
                print("Depósito realizado com sucesso!")
            elif operação == 3:
                valor = float(input("Digite o valor do saque: "))
                c.saque(valor)
                print("Saque realizado com sucesso!")
            operação = int(input("Digite 1 para consultar o saldo, digite 2 para realizar o depósito, digite 3 para sacar ou digite 0 para terminar a operação: "))
UI.main()