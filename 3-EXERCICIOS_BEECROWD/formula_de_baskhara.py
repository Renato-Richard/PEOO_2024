"""Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular".
Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto,
com uma mensagem correspondente conforme exemplo abaixo.
Imprima sempre o final de linha após cada mensagem."""

import math
a, b, c = input().split()
a = float(a[0])
b = float(b[1])
c = float(c[2])
delta = b ** 2 * 4 * a * c
if delta < 0:
    print("Impossivel calcular") 
else:
    x1 = -b + math.sqrt(delta) / 2 * a
    x2 = -b - math.sqrt(delta) / 2 * a
    print("R1 =", x1)
    print("R2 =", x2)
