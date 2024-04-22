# 1 -completo
# numeros = []
# for a in range(10):
#     crescente = int(input("Digite um número: "))
#     numeros.append(crescente)
# numeros.sort()
# print("Resultado", numeros)
# 2 - completo
# numeros_0 = []
# for b in range(10):
#     decrescente = int(input("Digite um número: "))
#     numeros_0.append(decrescente)
# numeros_0.sort(reverse=True)
# print("Resultado", numeros_0)

# 3
frase = input("Digite uma frase: ")
separador = frase.split(" ")
for c in range(len(separador)):
    separador.pop(0)
print(separador)

# 8 - completo
# frase_0 = input("Digite uma frase: ")
# separador = frase_0.split(" ")
# for palavra in separador:
#     print(palavra[-1])


# 11
# entrada_da_string_0 = input("Digite uma frase: ")
# separador_da_string = entrada_da_string_0.split(" ")

#15 - completo
# entrada_da_frase_0 = input("Digite uma frase: ").lower() #a função lower desconsidera as letras maiúsculas
# separador_da_frase = entrada_da_frase_0.split(" ")
# def contar_palavras(separador_da_frase):
#     count = 0
#     for palavra in separador_da_frase:
#         count += 1
#     return count # encerra a execução e retorna o valor da função
# print(contar_palavras(separador_da_frase))

#16 - completo
# frase_1 = input("Digite uma frase: ").lower()
# a, e, i, o, u = frase.count("a"), frase.count("e"), frase.count("i"), frase.count("o"), frase.count("u")
# print("A", a)
# print("E", e)
# print("I", i)
# print("O", o)
# print("U", u)


# 17 - incompleto

"""Ler uma frase e mostrar cada palavra repetidas vezes de acordo com o número de vogais.
(Desprezar os acentos)
Digite uma frase:
Tecnico em Informatica para Internet
Tecnico Tecnico Tecnico em Informatica Informatica Informatica Informatica Informatica para para Internet
Internet Internet"""

# frase = input("Digite uma frase: ")
# for palavra in frase:
#     vogais = frase.count("a"), frase.count("e"), frase.count("i"), frase.count("o"), frase.count("u")
# print(vogais)
