#
# Autores:
# Michel silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 27/06/2022
#
# 3. Desenvolva um programa em linguagem Python que após o   
# usuário informar uma certa quantidade de horas, minutos e  
# segundos, converta todo este tempo para segundos e         
# apresente-o em tela.                                       

# Entrada de dados

horas = int(input("Informe a quantidade de horas: ")) # Solicita a quantidade de horas
minutos = int(input("Informe a quantidade de minutos: ")) # Solicita a quantidade de minutos
segundos = int(input("Informe a quantidade de segundos: ")) # Solicita a quantidade de segundos

# Processamento de dados

total = (horas * 3600) + (minutos * 60) + segundos # Calcula o total de segundos

# Saída de dados

print(f"\nTotal de segundos: {total}s") # Imprime o total de segundos
print("fim do programa") # Informa ao usuário que o programa terminou
