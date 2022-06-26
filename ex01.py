#
# Autores:
# Michel silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 26/06/2022
#
# 1. Escreva um programa em linguagem Python que receba do   
# usuário três números reais e em seguida imprima-os em tela 
# na ordem inversa. Por exemplo, se o usuário informar os    
# números 15.55, 50.3 e -50.2, o programa deve imprimir em   
# tela estes mesmos números na seguinte sequência: -50.2,    
# 50.3 e 15.55.                                              

# Entrada de dados
valor1 = float(input("informe o valor 1: ")) # Solicita o primeiro valor
valor2 = float(input("informe o valor 2: ")) # Solicita o segundo valor
valor3 = float(input("informe o valor 3: ")) # Solicita o terceiro valor

# Saída de dados
print(f"entrada: {valor1}, {valor2}, {valor3}")  # imprime os valores de entrada
print(f"saída: {valor3}, {valor2}, {valor1}") # imprime os valores de saída
print("fim do programa") # informa ao usuário que o programa terminou
