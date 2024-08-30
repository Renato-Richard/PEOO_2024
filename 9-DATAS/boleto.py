import enum
import datetime
class Pagamento(enum.Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 4
class Boleto:
    def __init__(self, cod: str, emissao, venc, dataPgto, valorBoleto: float, valorPago: float, pagamento):
        self.__codBarras = ""
        self.__dataEmissao = emissao
        self.__dataVencimento = venc
        self.__dataPagto = dataPgto
        self.__valorBoleto = 0.0
        self.__valorPago = 0.0
        self.__situacaoPagamento = pagamento
        if cod != "": self.__codBarras = cod
        else: raise ValueError()
        if dataPgto != "": self.__dataPagto = dataPgto
        else: raise ValueError()
        if valorBoleto >= 0: self.__valorBoleto = valorBoleto
        else: raise ValueError()
        if valorPago >= 0: self.__valorPago = valorPago
        else: raise ValueError()
    def Pagar(self, valorPago):
        return self.__valorBoleto - self.__valorPago
    def Situacao(self):
        pass
    def __str__(self):
        pass
        # return f"O boleto de valor R${self.__valorBoleto}"
class UI:
    @staticmethod
    def menu():
        pass
    @staticmethod
    def main():
        pass
    @staticmethod
    def metodo():
        pass