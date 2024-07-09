class Cinema():
    def __init__(self):
        self.dia = " "
        self.horario = 0
    def tarifa(self):
        valor = 0
        if self.dia in ["segunda", "terça", "quinta"]:
            valor = 16.00
        elif self.dia == "quarta":
            valor = 8.00
        elif self.dia in ["sexta", "sábado", "domingo"]:
            valor = 20.00
        if 17 <= self.horario < 24:
            valor *= 1.5
        return valor
c = Cinema()
c.dia = input("Digite o dia da sessão. Ex.: Segunda.: ")
c.horario = float(input("Digite o horário da sessão. Ex.: 17.: "))
valor = c.tarifa()
print(f"O ingresso vale: R$ {valor:.2f}")
