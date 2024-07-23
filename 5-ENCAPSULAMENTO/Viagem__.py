class Viagem:
    def __init__(self):
        self.__km = 0
        self.__h = 0
        self.__min = 0
    def set_distancia(self, v_d):
        if v_d > 0: self.__km = v_d
        else: raise ValueError("A distância deve ser um número positivo")
    def set_tempo(self, v_h, v_m):
        if v_h > 0: self.__h = v_h
        else: raise ValueError("O tempo deve ser um número positivo")
        if v_m > 0: self.__min = v_m
        else: raise ValueError("O tempo deve ser um número positivo")
    def get_distancia(self):
        return self.__km
    def get_tempo(self):
        return self.__h, self.__min
    def velocidade_media(self):
        tempo = self.__h + self.__min / 60
        if tempo > 0: return tempo
        else: raise ValueError("O tempo total deve ser maior que zero.")
class UI:
    @staticmethod
    def main():
        vm = Viagem()
        quilômetros = float(input("Digite os quilômetros: "))
        horas = float(input("Digite o tempo em horas: "))
        minutos = float(input("Digite o tempo em minutos: "))
        vm.set_distancia(quilômetros)
        vm.set_tempo(horas, minutos)
        print(f"Velocidade média: {vm.velocidade_media():.2f} km/h")
UI.main()