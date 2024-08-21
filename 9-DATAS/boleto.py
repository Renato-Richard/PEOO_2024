import enum
import datetime
class Pagamento(enum.Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 4
class Boleto:
    def __init__(self):
        self.codBarras = ""
        self.dataEmissao = ""
        self.dataPagto = ""
        self.valorBoleto = 0.0
        self.valorPago = 0.0
        self.situacaoPagamento = Pagamento
    def Boleto(self):
        pass
    def Pagar(self):
        pass
    def Situacao(self):
        pass
    def __str__(self):
        return