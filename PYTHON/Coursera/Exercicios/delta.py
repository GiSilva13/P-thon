#Feito por mim#
import math
a = int(input("Diite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
delta = b**2 - 4 * a *c

if delta > 0:
    print("A equação tem duas raizes reais diferentes")
elif delta == 0:
    print("A equação tem uma raiz real dupla")

elif delta < 0:
    print("A equação não tem raízes reais")

#Feito pela internet#

print("-------------------------------------------------------")

import math 

#Entrada de dados#
a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
c = int(input("Digite um valor para C: "))

#Calculo do delta#
delta = b*b - 4 * a * c

#testes#
if delta < 0:
    print("A equação não possui raizes reais.")
elif delta == 0:
    raiz = (-1*b + math.sqrt(delta))/(2 * a)
    print("A equacao possui apenas uma raiz que e ",raiz)
elif delta > 0:
    raiz1 =(-1*b + math.sqrt(delta))/(2 * a)
    raiz2 =(-1*b + math.sqrt(delta))/(2 * a)
    print("As raizes da equacao sao ",raiz1, "e",raiz2)

    
