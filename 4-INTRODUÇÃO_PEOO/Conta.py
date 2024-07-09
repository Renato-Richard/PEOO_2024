class Conta():
    def __init__(self):
        self.titular = " "
        self.nConta = " "
        self.saldo = 0
    def depósito(self, valor):
        self.saldo = self.saldo + valor
    def saque(self, valor):
        self.saldo = self.saldo - valor
c = Conta()
c.titular = input("Nome do titular: ")
c.nConta = input("Número da conta: ")
operação = int(input("Digite 1 para consultar o saldo, digite 2 para realizar o depósito, digite 3 para sacar ou digite 0 para terminar a operação."))
while operação != 0:
    if operação == 1:
        print(c.saldo)
    elif operação == 2:
        valor = int(input("Digite o valor do depósito: "))
        c.depósito(valor)
        print("Depósito realizado com sucesso!")
    elif operação == 3:
        valor = int(input("Digite o valor do saque: "))
        c.saque(valor)
        print("Saque realizado com sucesso!")
    operação = int(input("Digite 1 para consultar o saldo, digite 2 para realizar o depósito, digite 3 para sacar ou digite 0 para terminar a operação."))