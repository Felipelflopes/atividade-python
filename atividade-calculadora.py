#3-	Crie uma calculadora simples receba dois números, 
#de a opção do usuário escolher a operação e ao clicar
# em um botão exiba o resultado da operação.

import os

os.system ("cls")

print("---> Atividade Calculadora Simples <---")
print("---------------------------------------")

a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))

print("Escolha a operação desejada")
opera = int(input(" 1 para SOMAR \n 2 para DIMINUIR \n 3 para MULTIPLICAR \n 4 para DIVIDIR \n"))

if opera == 1:
    resultado = a + b
elif opera == 2:
    resultado = a - b
elif opera == 3:
    resultado = a * b
elif opera == 4:
    resultado = a / b
else:
    print("Operação inválida!")
    resultado = 0

print("-------------------------------------")   
print("Resultado: ", resultado)


print("-------------------------------------")
input("Pressione <ENTER> para continuar...")
