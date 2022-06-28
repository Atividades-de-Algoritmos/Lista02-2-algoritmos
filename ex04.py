#
# Autores:
# Michel silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 27/06/2022
#
# 4. Implemente um programa em linguagem Python que seja     
# capaz de efetuar contagem de dinheiro. Para isso, o usuário
# do programa deve informar a quantidade de notas de         
# •	2 reais;                                                 
# •	5 reais;                                                 
# •	10 reais;                                                
# •	20 reais;                                                
# •	50 reais;                                                
# •	100 reais                                                
# e o programa deve imprimir na tela a quantidade de notas de
# cada valor informado.                                      

# Entrada de dados

nota2 = int(input("informe a quantidade de notas de 2 reais: ")) # Solicita a quantidade de notas de 2 reais
nota5 = int(input("informe a quantidade de notas de 5 reais: ")) # Solicita a quantidade de notas de 5 reais
nota10 = int(input("informe a quantidade de notas de 10 reais: ")) # Solicita a quantidade de notas de 10 reais
nota20 = int(input("informe a quantidade de notas de 20 reais: ")) # Solicita a quantidade de notas de 20 reais
nota50 = int(input("informe a quantidade de notas de 50 reais: ")) # Solicita a quantidade de notas de 50 reais
nota100 = int(input("informe a quantidade de notas de 100 reais: ")) # Solicita a quantidade de notas de 100 reais
nota200 = int(input("informe a quantidade de notas de 200 reais: ")) # Solicita a quantidade de notas de 200 reais

# Processamento de dados

total = (nota2 * 2) + (nota5 * 5) + (nota10 * 10) + (nota20 * 20) + (nota50 * 50) + (nota100 * 100) + (nota200 * 200) # Calcula o valor total das notas

# Saída de dados

print(f"total: R${total}") # Imprime o total monetário em reais
print("fim do programa") # Informa ao usuário que o programa terminou
