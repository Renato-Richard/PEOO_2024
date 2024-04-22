# 1
# entrada_0 = int(input())
# entrada_1 = int(input())
# if a > b:
#     print(f'Maior = {a}')
# else:
#     print(f'Maior = {b}')
# 2
# valor_0 = float(input())
# valor_1 = float(input())
# valor_2 = float(input())
# valor_3 = float(input())
# media_aritmetica_simples = (valor_0 + valor_1 + valor_2 + valor_3) / 4
# print(f'Média = {media_aritmetica_simples}')
# lista_minima = []
# if valor_0 < media_aritmetica_simples:
#     lista_minima.append(valor_0)
#     if valor_1 < media_aritmetica_simples:
#         lista_minima.append(valor_1)
#         if valor_3 < media_aritmetica_simples:
#             lista_minima.append(valor_3)
# print(f"Números menores que a média: {lista_minima}")
# lista_maxima = []
# if valor_0 >= media_aritmetica_simples:
#     lista_maxima.append(valor_0)
#     if valor_1 >= media_aritmetica_simples:
#         lista_maxima.append(valor_1)
#         if valor_2 >= media_aritmetica_simples:
#             lista_maxima.append(valor_2)
#             if valor_3 >= media_aritmetica_simples:
#                 lista_maxima.append(valor_3)
# print(f"Números maiores ou iguais à média: {lista_maxima}")

# 3
# lista_pares = []
# lista_impares = []
# for entradas in range(4):
#     par_impar = int(input("Digite um número: "))
#     if par_impar % 2 == 0: lista_pares.append(par_impar)
#     else: lista_impares.append(par_impar)
# print("Soma dos pares = ", sum(lista_pares))
# print("Soma dos ímpares = ", sum(lista_impares))

# 4 - incompleto
# lista_horas = []
# horario_1, horario_2 = input("Digite o primeiro horário no formato hh:mm: "), input("Digite o segundo horário no formato hh:mm: ")
# conversao = int(horario_1.split(0:4))
# print(horario_1)

# 5 - incompleto

# entrada: inteiro
    # não pode ser maior que 12
# 12 / 4 = 3
# numero_mes = int(input("Digite um número até 12: "))
# primeiro_trimestre, segundo_trimestre, terceiro_trimestre, quarto_trimestre = (numero_mes <= 1 // 4 * 12), (4, 5, 6), (7, 8, 9), (10, 11, 12)
# if numero_mes > 12:
#     print("Erro. Digite novamente um número somente até 12.")
# elif numero_mes == primeiro_trimestre:
#     print(primeiro_trimestre)

# 6
# lista_valores = []
# for min_max in range(3):
#     max_min = int(input("Digite um número: "))
#     lista_valores.append(max_min)
# max, min = max(lista_valores), min(lista_valores)
# print("A soma do maior com o menor número é: ", max + min)

# 7

# import math
# print("Digite os coeficientes a, b, e c de uma equação do II grau:")
# coeficiente_a = int(input("a: "))
# coeficiente_b = int(input("b: "))
# coeficiente_c = int(input("c: "))
# delta = coeficiente_b ** 2 - 4 * coeficiente_a * coeficiente_c
# if delta < 0:
#     print("Impossível calcular.")
# elif delta >= 0:
#     x1 = (-coeficiente_b + math.sqrt(delta)) / 4 * coeficiente_a
#     x2 = (-coeficiente_b - math.sqrt(delta)) / 4 * coeficiente_a
#     print("As raízes são", int(x1), "e", int(x2))

# 8

# lista_atualizada = []
# for menor_maior in range(4):
#     maior_menor = int(input("Digite um número: "))
#     lista_atualizada.append(maior_menor)
# print("Maior valor = ", max(lista_atualizada))
# print("Menor valor = ", min(lista_atualizada))
# lista_atualizada.remove(max(lista_atualizada))
# lista_atualizada.remove(min(lista_atualizada))
# print("A soma do segundo maior valor com o segundo menor = ", max(lista_atualizada) + min(lista_atualizada))

# 9 - incompleto

"""Ler a quantidade de horas e minutos marcados em um relógio analógico e calcular o menor ângulo formado
entre os ponteiros do relógio. Mostrar uma mensagem de “Hora Inválida” se os valores fornecidos não formarem
uma hora válida.
Digite o horário no formato hh:mm
03:30
Menor ângulo entre os ponteiros = 75 graus"""

# f_horario = input()

# 10 - incompleto

"""Ler uma data no formato "dd/mm/aaaa" e verificar se é uma data válida, considerando como válidos os anos
entre 1900 e 2100, meses de 1 a 12 e dias de acordo com o mês.
Digite uma data no formato dd/mm/aaaa
32/08/2013
A data informada não é válida"""

# def_horario = input("Digite uma data no formato dd/mm/aaaa: ")
# separador = def_horario.split("/")
# dia, mes, ano = int(separador[0]), int(separador[1]), int(separador[2])
# # print(dia, mes, ano)
# if 1900 < ano > 2100 or mes > 12:
#     print("A data informada não é válida")
# elif mes == 1 and 3 and 5 and 7 and 8 and 10 and 12:
#     print("Algum é verdadeiro")
#     if dia > 31:
#         print("A data informada não é válida")
# elif mes == 4 and 6 and 9 and 11:
#     if dia > 30:
#         print("A data informada não é válida_2")
    
# else:
#     print("A data informada não é válida")
        # print("deu certo")
        # if mes == 4 or 6 or 9 or 11:
        #     dia <= 30
        #     print("Aqui que deu certo")


# se o dígito do mês for 12, o dia vai até 31
# se o dígito do mês for 11, o dia vai até 30
# se o dígito do mês for 10, o dia vai até 31
# se o dígito do mês for 9, o dia vai até 30
# se o dígito do mês for 8, o dia vai até 31
# se o dígito do mês for 7, o dia vai até 31
# se o dígito do mês for 6, o dia vai até 30
# se o dígito do mês for 5, o dia vai até 31
# se o dígito do mês for 4, o dia vai até 30
# se o dígito do mês for 3, o dia vai até 31
# se o dígito do mês for 2, o ano vai ser dividido por 4, se resultar num inteiro, o dia vai até 29, se resultar num float, são 28 dias
# se o dígito do mês for 1, o dia vai até 31

# dividir 365 para 12
# horas: 24 * dia do mês
# dia: dia do mês 
# cálculo do ano bissexto: ano // 4: se for inteiro, é bissexto, se não, não é

"""Janeiro: 31 dias
Fevereiro: 28 ou 29 dias (dependendo se é um ano bissexto)
Março: 31 dias
Abril: 30 dias
Maio: 31 dias
Junho: 30 dias
Julho: 31 dias
Agosto: 31 dias
Setembro: 30 dias
Outubro: 31 dias
Novembro: 30 dias
Dezembro: 31 dias"""

"""
if separador[1] > 12:
    for >= 31 """

# 13 - incompleto


# for v in range(10):
#     v2 = input() .split(" ")
#     v1 = v2
# print(v)

# v = input() .split()
# for 
# v1 = int(v[0])
# v2 = int(v[1])
# v3 = int(v[2])
# v4 = int(v[3])
# v5 = int(v[4])
# v6 = int(v[5])
# v7 = int(v[6])
# v8 = int(v[7])
# v9 = int(v[8])
# v10 = int(v[9])
# vss = v1, v2, v3, v4, v5, v6, v7, v8, v9, v10
# listall = []
# listall.append(vss)
# print(listall)

#14 - incompleto

"""Ler três valores e dizer se eles formam um triângulo.
Caso afirmativo, dizer seu tipo (equilátero, isósceles ou escaleno).
Digite três valores:
1
2
10
Esses valores não formam um triângulo"""

# for t in range(3):
#   triangulo = int(input("Digite três valores: "))
# print("Esses valores não formam um triângulo")

#15
lista_desordenada_ordenada = []
for c in range(3):
    crescente = int(input("Digite três valores: "))
    lista_desordenada_ordenada.append(crescente)
lista_desordenada_ordenada.sort()
print(lista_desordenada_ordenada)