class Cinema:
    def __init__(self):
        self.__dia = " "
        self.__horario = 0
    def set_dia(self, v):
        if v in ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]: self.__dia = v
        else: raise ValueError("Digite o dia da sessão corretamente. Ex.: Segunda.")
    def set_horario(self, v):
        if 1 <= v < 24: self.__horario = v
        else: raise ValueError("Digite um horário válido para a sessão. Ex.: 17.")
    def get_dia(self):
        return self.__dia
    def get_horario(self):
        return self.__horario
    def tarifa(self):
        valor = 0
        if self.__dia in ["segunda", "terça", "quinta"]:
            valor = 16.00
        elif self.__dia == "quarta":
            valor = 8.00
        elif self.__dia in ["sexta", "sábado", "domingo"]:
            valor = 20.00
        if 17 <= self.__horario < 24:
            valor *= 1.5
        return valor
class UI:
    @staticmethod
    def main():
        c = Cinema()
        diaSessão = input("Digite o dia da sessão. Ex.: Segunda.: ")
        horarioSessão = float(input("Digite o horário da sessão. Ex.: 17.: "))
        c.set_dia(diaSessão)
        c.set_horario(horarioSessão)
        print(f"O ingresso vale: R$ {c.tarifa():.2f}")
UI.main()