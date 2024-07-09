class Circulo():
    def __init__ (self):
        self.raio = 0
    def calc_a(self):
        return 3.14 * self.raio ** 2 
    def calc_c(self):
        return 2 * 3.14 * self.raio
c = Circulo()
c.raio = float(input("Digite o raio do círculo: "))
print(c.calc_a(), c.calc_c())