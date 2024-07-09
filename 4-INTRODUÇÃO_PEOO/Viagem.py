class Viagem():
    def __init__(self):
        self.km = 0
        self.h = 0
        self.min = 0
    def velocidadeMedia(self):
        velocidade_media = self.km / self.h
        return velocidade_media
vm = Viagem()
vm.km = float(input("Digite os quilômetros: "))
vm.h = int(input("Digite o tempo em horas: "))
vm.min = int(input("Digite o tempo em minutos: "))
horas = vm.h + vm.min / 60
velocidade = vm.velocidadeMedia()
print(f"Velocidade média: {velocidade:.2f} km/h")