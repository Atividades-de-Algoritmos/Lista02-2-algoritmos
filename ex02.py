#
# 	Elabore um programa em linguagem Python que tem como objetivo calcular a área
# 	de um círculo. Para isso, o seu programa deve receber como entrada o raio
# 	deste círculo em centímetros. Lembre-se que o cálculo de área de um círculo
# 	é dado por A=πR^2, em que R é o raio do círculo e π é aproximadamente igual a 3.1416.
#   O programa deve imprimir na tela o valor da área do círculo.
#

# entrada de dados
raio = float(input("informe o raio: ")) # recebe o raio

# processamento
area = 3.1416 * (raio ** 2) # calcula a area

# saida de dados
print(f"A área do círculo é: {area}") # imprime a area

