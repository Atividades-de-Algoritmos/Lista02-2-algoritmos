#
# Autores:
# Michel silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 27/06/2022
#
# 2. Elabore um programa em linguagem Python que tem como    
# objetivo calcular a área de um círculo. Para isso, o seu   
# programa deve receber como entrada o raio deste círculo em 
# centímetros. Lembre-se que o cálculo de área de um círculo 
# é dado por A=πR^2, em que R é o raio do círculo e π é      
# aproximadamente igual a 3.1416. O programa deve imprimir na
# tela o valor da área do círculo.                           

# Entrada de dados

raio = float(input("informe o raio: ")) # Solicitando o raio do círculo

# Processamento de dados

area = 3.1416 * (raio ** 2) # Calcula a área do círculo

# Saída de dados

print(f"A área do círculo é: {area}") # Imprime a área do círculo
print("fim do programa") # Informa ao usuário que o programa terminou
