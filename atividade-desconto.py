#4-	Crie um programa em PYTHON para receber: 
# a descrição do produto (nome), a quantidade 
# adquirida e o preço unitário. Após receber os dados, 
# o programa deve calcular e exibir o total e o total 
# a pagar com desconto conforme abaixo: 

#Fórmula para calcular o Total (sem desconto)
#Total = quantidade adquirida * preço unitário;

#O desconto é retirado do total a partir da tabela de quantidades abaixo:
#•	Se quantidade <= 5 o desconto será de 2%
#•	Se quantidade > 5 e quantidade <=10 o desconto será de 3%
#•	Se quantidade > 10 o desconto será de 5%
#Fórmula para calcular o Total (sem desconto)
#Total a pagar = (total – desconto).

import os

os.system ("cls")

print("---> Atividade - Calculando Desconto <----")
print("------------------------------------------")

# 1 Passo - Entrada
produto_nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade desejada: "))
p_unitario = float(input("Digite o valor do produto: "))

# 2 Passo - Processamento

#Calculando o Total sem desconto
total = quantidade * p_unitario

print("------------------------------------------")
print("Sua compra foi: ", total)
print("------------------------------------------")

if quantidade <= 5:
    a=total*0.02
    desconto = total-a
    print("Desconto será de *2%* - Total ---> R$", desconto)

elif quantidade > 5 and quantidade <= 10:
    b=total*0.03
    desconto = total-b
    print("Desconto será de *3%* - Total ---> R$", desconto)

elif quantidade > 10:
    c=total*0.05
    desconto = total-c
    print("Desconto será de *5%* - Total ---> R$", desconto)
else:
    print("*Valor sem desconto*")


print("------------------------------------------")
input("Pressione <ENTER> para continuar...")
