#
# 4.	Implemente um programa em linguagem Python que seja capaz de efetuar contagem de dinheiro.
# Para isso, o usuário do programa deve informar a quantidade de notas de
# •	2 reais;
# •	5 reais;
# •	10 reais;
# •	20 reais;
# •	50 reais;
# •	100 reais
# e o programa deve imprimir na tela a quantidade de notas de cada valor informado.
#
#entrada de dados
nota2 = int(input("informe a quantidade de notas de 2 reais: ")) # recebe a quantidade de notas de 2 reais
nota5 = int(input("informe a quantidade de notas de 5 reais: ")) # recebe a quantidade de notas de 5 reais
nota10 = int(input("informe a quantidade de notas de 10 reais: ")) # recebe a quantidade de notas de 10 reais
nota20 = int(input("informe a quantidade de notas de 20 reais: ")) # recebe a quantidade de notas de 20 reais
nota50 = int(input("informe a quantidade de notas de 50 reais: ")) # recebe a quantidade de notas de 50 reais
nota100 = int(input("informe a quantidade de notas de 100 reais: ")) # recebe a quantidade de notas de 100 reais

# processamento
total = (nota2 * 2) + (nota5 * 5) + (nota10 * 10) + (nota20 * 20) + (nota50 * 50) + (nota100 * 100) # calcula o total de notas

# saida de dados
print(f"total de notas: {total}") # imprime o total de notas
