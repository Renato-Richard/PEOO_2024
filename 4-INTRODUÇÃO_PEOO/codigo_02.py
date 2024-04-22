class aluno:
    def __init__(self): #construtor
        self.nome = ''
        self.matricula = ''
    def ano_de_ingresso(self):
        return int(self.matricula[0,4])

a = aluno()
a.nome = 'Renato'
a.matricula = '20221011110022'
b = aluno()
b.matricula = '20221011110022'

print(a.nome, a.matricula, a.ano_de_ingresso())
print(b.nome, b.matricula, b.ano_de_ingresso())