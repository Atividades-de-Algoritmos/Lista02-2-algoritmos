#
# Autores:
# Michel silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 26/06/2022
#
# 3. Desenvolva um programa em linguagem Python que após o   
# usuário informar uma certa quantidade de horas, minutos e  
# segundos, converta todo este tempo para segundos e         
# apresente-o em tela.                                       

# Entrada de dados
horas = int(input("informe a quantidade de horas: ")) # recebe a quantidade de horas
minutos = int(input("informe a quantidade de minutos: ")) # recebe a quantidade de minutos
segundos = int(input("informe a quantidade de segundos: ")) # recebe a quantidade de segundos

# Processamento
total = (horas * 3600) + (minutos * 60) + segundos # calcula o total de segundos

# Saída de dados
print(f"\ntotal de segundos: {total}s") # imprime o total de segundos
print("fim do programa") # informa ao usuário que o programa terminou
