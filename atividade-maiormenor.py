#1 - Crie um programa em PYTHON que receba 2 valores e exiba para o usuário o MAIOR e MENOR valor, 
# caso algum dos números inseridos forem iguais, 
# o programa deve informar ao usuário que os valores são iguais.

import os

os.system ("cls")

print(" ---> Atividade Maior e Menor Valor <---")
print("----------------------------------------")

# 1 Passo - Entrada
valor01 = int(input("Digite o primeiro valor: "))
valor02 = int(input("Digite o segundo valor: "))
print("----------------------------------------")

# 2 Passo - Processamento / Saída
if valor01 > valor02:
    print("O maior valor é:", valor01, "e menor valor é:", valor02 )

elif valor02 > valor01:
    print("O maior valor é:", valor02, "e menor valor é:", valor01)

else:
    print("Os valores são Iguais")    

print("----------------------------------------")
input("Pressione <ENTER> para continuar...")
