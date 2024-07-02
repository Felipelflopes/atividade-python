#5-	A escola “APRENDER” faz o pagamento de seus professores por hora/aula.
# Crie um programa em Visual PYTHON que receba o nível do professor, 
#a qtd de aulas por semana, em seguida calcule e exiba o salário total do professor. 

#Valor da hora/aula:
#•	Professor Nível 1 - R$ 12,00 por hora/aula
#•	Professor Nível 2 - R$ 17,00 por hora/aula
#•	Professor Nível 3 - R$ 25,00 por hora/aula

import os

os.system ("cls")

print(" ----------> Atividade 05 <---------- ")
print("-------------------------------------")


nivel = int(input("Informe o seu nível (1, 2 , 3), por favor: "))
aulas = float(input("Informe a quantidade de aulas: "))
print("-------------------------------------")

if nivel==1:
    salario = aulas*12
    print(" A quantidade de aulas foi de {:.2f},\n Corresponde a um salário de R$ {:.2f}.".format(aulas,salario))
elif nivel==2:
    salario = aulas*17
    print(" A quantidade de aulas foi de {:.2f},\n Corresponde a um salário de R$ {:.2f}.".format(aulas,salario))
elif nivel==3:
    salario = aulas*25
    print(" A quantidade de aulas foi de {:.2f},\n Corresponde a um salário de R$ {:.2f}.".format(aulas,salario))
else:
    print("<Opção Inválida: --- Reinicie o programa para tentar novamente")


print("-------------------------------------")
input("Pressione <ENTER> para continuar...")
