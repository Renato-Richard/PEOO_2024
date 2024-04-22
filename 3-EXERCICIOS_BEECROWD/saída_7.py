# saída 7
variavel = 97
lista_das_variaveis = []
lista_das_variaveis.append(variavel)
for i in range(25):
    variavel = variavel + 1
    lista_das_variaveis.append(variavel)
ordenacao = ord("a") # imprime números de acordo com a letra
print(lista_das_variaveis[0], "e", "a")
lista_das_variaveis.pop(0)
for c in range(26):
    ordenacao = ordenacao + 1
    print(lista_das_variaveis[0], "e", chr(ordenacao)) # a função chr converte a função ord em letras
    lista_das_variaveis.pop(0)