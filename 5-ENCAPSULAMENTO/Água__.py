class Agua:
    def __init__(self):
        self.__mes = 0
        self.__ano = 0
        self.__consumo = 0
    def set_mes_ano(self, x, y):
        if 0 < self.__mes <= 12: self.__mes = x
        else: raise ValueError("Insira o dígito de mês válido.")
        if self.__ano > 0: self.__ano = y
        else: raise ValueError("Dígitos do ano inválidos")
    def set_consumo(self, x):
        if self.__consumo > 0: self.__consumo = x
        else: raise ValueError("Dígitos do consumo inválidos")
    def get_mes_ano(self):
        return self.__mes, self.__ano
    def get_consumo(self):
        return self.__consumo
    def calc_litros(self):
        valor = 38.00
        for i in range(self.__consumo):
            if 11 <= i <= 20: valor += 5
            if i > 21: valor += 11
class UI:
    @staticmethod
    def main():
        a = Agua()
        mes = int(input("Digite o mês correspondente:"))
        ano = int(input("Digite o ano: "))
        consumo = int(input("Digite o consumo em m³: "))
        a.set_mes(mes), a.set_ano(ano), a.set_consumo(consumo)
        print(f"O consumo de {consumo}m³ do mês {mes} do ano de {ano} possui o valor de R$")