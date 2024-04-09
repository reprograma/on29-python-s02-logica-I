#Questão 16 - Programa para loja de tintas

import math

#Solicitando ao usuário a área a ser pintada
area_pintura = float(input("\nInforme a área a ser pintada em m²: "))

#Calculando o consumo de tinta em função da área informada
consumo_tinta = area_pintura / 3

#Calculando o número de latas em função do consumo calculado
numero_latas = (consumo_tinta / 18)
numero_latas = math.ceil(numero_latas)

#Calculando o valor total em função do número de latas necessário
valor_total = (numero_latas * 80)
texto_valor_total = f"R${valor_total:_.2f}"
texto_valor_total = texto_valor_total.replace(".", ",").replace("_", ".")

print(f"\nPara pintura da área informada serão necessárias {numero_latas} latas.")
print(f"O valor total da compra é de {texto_valor_total}.")
