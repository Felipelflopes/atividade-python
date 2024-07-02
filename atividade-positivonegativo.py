#2-	Escreva um programa em PYTHON que solicite ao 
# usuário para inserir um número e, em seguida, 
# determine se o número é positivo, negativo ou zero, 
# e imprima essa informação.

import os

os.system ("cls")

print(" ---> Atividade - Número Positivo ou Negativo  <---")
print("---------------------------------------------------")

# 1 Passo - Entrada
numero = float(input("Digite um número: "))
print("--------------------------------------------------")

# 2 Passo - Processamento / Saída
if numero > 0:
    print("O Número digitado é --------------> *POSITIVO*")

elif numero < 0:
    print("O Número é -----------------------> *NEGATIVO*")

else:
    print("O número é --------------------------> *ZERO*")

print("--------------------------------------------------")
input("Pressione <ENTER> para continuar...")
