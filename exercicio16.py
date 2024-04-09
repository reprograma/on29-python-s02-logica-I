#exercicio16.py

import math

# Definindo o preço e a capacidade da lata de tinta
preco_lata = 80.00
capacidade_lata = 18

# Pedindo ao usuário o tamanho da área a ser pintada em metros quadrados
tamanho_area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Calculando a quantidade de tinta necessária em litros
litros_tinta = tamanho_area / 3

# Calculando o número de latas necessárias
latas_necessarias = math.ceil(litros_tinta / capacidade_lata)

# Calculando o preço total
preco_total = latas_necessarias * preco_lata

# Exibindo a quantidade de latas necessárias e o preço total para o usuário
print("Quantidade de latas necessárias:", latas_necessarias)
print("Preço total: R$", preco_total)
