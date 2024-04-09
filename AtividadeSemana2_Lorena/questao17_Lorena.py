#Questão 17 - Programa para loja de tintas

import math

#Solicitando ao usuário a área a ser pintada
area_pintura = float(input("\nInforme a área a ser pintada em m²: "))

#Calculando o consumo de tinta em função da área informada
rendimento_tinta_m2 = 6.0
consumo_tinta = area_pintura / rendimento_tinta_m2
consumo_tinta_folga = consumo_tinta * 1.1

#Calculando a quantidade de latas de 18 litros
volume_lata = 18.0
quantidade_latas = (consumo_tinta / volume_lata)
quantidade_latas = math.ceil(quantidade_latas)

#Calculando o valor total de latas 
valor_unitario_lata = 80
valor_total_latas = (quantidade_latas * valor_unitario_lata)
texto_valor_total_latas = f"R${valor_total_latas:_.2f}"
texto_valor_total_latas = texto_valor_total_latas.replace(".", ",").replace("_", ".")

#Calculando a quantidade de galões de 3,6 litros
volume_galao = 3.6
quantidade_galoes = (consumo_tinta / volume_galao)
quantidade_galoes = math.ceil(quantidade_galoes)

#Calculando o valor total de galões
valor_unitario_galao = 25
valor_total_galoes = (quantidade_galoes * valor_unitario_galao)
texto_valor_total_galoes = f"R${valor_total_galoes:_.2f}"
texto_valor_total_galoes = texto_valor_total_galoes.replace(".", ",").replace("_", ".")

#Calculando a quantidade otimizada de latas e galões em função da área informada
def otimizar_consumo_tinta ():
    if consumo_tinta_folga % volume_lata == 0:
        quantidade_latas_otimizada = consumo_tinta_folga / volume_lata
        valor_total_otimizado = quantidade_latas_otimizada * valor_unitario_lata
        texto_valor_total_otimizado = f"R${valor_total_otimizado:_.2f}"
        texto_valor_total_otimizado = texto_valor_total_otimizado.replace(".", ",").replace("_", ".")
    else:
        quantidade_latas_otimizada = int(consumo_tinta_folga // volume_lata)
        quantidade_galoes_otimizada = math.ceil((consumo_tinta_folga % volume_lata) / volume_galao)
        valor_total_otimizado = (quantidade_latas_otimizada * valor_unitario_lata) + (quantidade_galoes_otimizada * valor_unitario_galao)
        texto_valor_total_otimizado = f"R${valor_total_otimizado:_.2f}"
        texto_valor_total_otimizado = texto_valor_total_otimizado.replace(".", ",").replace("_", ".")


    return quantidade_latas_otimizada, quantidade_galoes_otimizada, texto_valor_total_otimizado


parametros_otimizados = otimizar_consumo_tinta()

print(f"\nOPÇÃO 1 (utilizando somente latas): para pintura da área informada serão necessárias  {quantidade_latas} latas.")
print(f"O valor total da compra em caso de escolha OPÇÃO 1 é de {texto_valor_total_latas}.")
       
print(f"\nOPÇÃO 2 (utilizando somente galões): para pintura da área informada serão necessários  {quantidade_galoes} galões.")
print(f"O valor total da compra em caso de escolha OPÇÃO 2 é de {texto_valor_total_galoes}.")

print(f"\nOPÇÃO 3 (considerando uma perda de 10%, e otimizando o uso entre latas e galões): para pintura da área informada serão necessárias {parametros_otimizados[0]} latas e {parametros_otimizados[1]} galões.")
print(f"O valor total da compra em caso de escolha OPÇÃO 3 é de {parametros_otimizados[2]}.")