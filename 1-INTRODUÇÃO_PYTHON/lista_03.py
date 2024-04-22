#1 e 2
primeiro_nome = input("Digite seu primeiro nome: ")
print(f"Bem-vindo ao Python, {primeiro_nome}")
nome_completo = input("Digite seu nome completo: ")
if " " in nome_completo:
    primeiro_nome_completo = nome_completo.split(" ")
    print(f"Bem-vindo ao Python, {primeiro_nome_completo[0]}")
#3
primeiro_bimestre = int(input("Digite a nota do primeiro bimestre da disciplina: "))
segundo_bimestre = int(input("Digite a nota do segundo bimestre da disciplina: "))
media_parcial = ((primeiro_bimestre * 2) + (segundo_bimestre * 3)) // (2 + 3)
print(f"Média parcial = {media_parcial}")
#4
import math
base, altura = input().split()
base = float(base)
altura = float(altura)
area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt((base ** 2) + (altura ** 2))
print(f"Área = {area} - Perímetro = {perimetro} - Diagonal = {diagonal}")