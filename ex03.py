#
#
# Autores:
# michel silva
#
#
# data: 26/06/2022

# 3.	Desenvolva um programa em linguagem Python que após o usuário informar uma certa quantidade de horas,
# minutos e segundos, converta todo este tempo para segundos e apresente-o em tela.
#
#entrada de dados
horas = int(input("informe a quantidade de horas: ")) # recebe a quantidade de horas
minutos = int(input("informe a quantidade de minutos: ")) # recebe a quantidade de minutos
segundos = int(input("informe a quantidade de segundos: ")) # recebe a quantidade de segundos

# processamento
total = (horas * 3600) + (minutos * 60) + segundos # calcula o total de segundos

# saida de dados
print(f"total de segundos: {total}") # imprime o total de segundos
