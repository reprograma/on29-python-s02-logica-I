#exercicio17.py

import math

# Definindo o preço e a capacidade da lata de tinta
preco_lata = 80.00
capacidade_lata = 18
preco_galao = 25.00
capacidade_galao = 3.6

# Função para calcular a quantidade de tinta necessária com 10% de folga
def calcular_quantidade_tinta(area):
    return math.ceil(area / 6 * 1.1)

# Função para calcular o preço total de compra de latas
def calcular_preco_latas(qtd_tinta):
    qtd_latas = math.ceil(qtd_tinta / capacidade_lata)
    preco_total = qtd_latas * preco_lata
    return qtd_latas, preco_total

# Função para calcular o preço total de compra de galões
def calcular_preco_galoes(qtd_tinta):
    qtd_galoes = math.ceil(qtd_tinta / capacidade_galao)
    preco_total = qtd_galoes * preco_galao
    return qtd_galoes, preco_total

# Função para calcular o preço total de mistura de latas e galões
def calcular_preco_mistura(qtd_tinta):
    qtd_latas = math.floor(qtd_tinta / capacidade_lata)
    qtd_galoes = math.ceil((qtd_tinta % capacidade_lata) / capacidade_galao)
    preco_total = qtd_latas * preco_lata + qtd_galoes * preco_galao
    return qtd_latas, qtd_galoes, preco_total

# Pedindo ao usuário o tamanho da área a ser pintada em metros quadrados
tamanho_area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Calculando a quantidade de tinta necessária em litros
qtd_tinta = calcular_quantidade_tinta(tamanho_area)

# Calculando as opções de compra
qtd_latas, preco_latas = calcular_preco_latas(qtd_tinta)
qtd_galoes, preco_galoes = calcular_preco_galoes(qtd_tinta)
qtd_latas_mistura, qtd_galoes_mistura, preco_mistura = calcular_preco_mistura(qtd_tinta)

# Exibindo os resultados
print("\nComprar apenas latas de 18 litros:")
print("Quantidade de latas:", qtd_latas)
print("Preço total:", preco_latas)

print("\nComprar apenas galões de 3,6 litros:")
print("Quantidade de galões:", qtd_galoes)
print("Preço total:", preco_galoes)

print("\nMisturar latas e galões:")
print("Quantidade de latas:", qtd_latas_mistura)
print("Quantidade de galões:", qtd_galoes_mistura)
print("Preço total:", preco_mistura)
