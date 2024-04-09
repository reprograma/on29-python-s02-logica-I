import math

area = float(input("Insira a quantidade, em metros quadrados, de área a ser pintada: "))
area_com_folga = area*1.1

litros_tinta = math.ceil(area_com_folga/6)

quant_latas = (litros_tinta-(litros_tinta%18))/18
quant_galoes = math.ceil((litros_tinta%18)/3.6)

valor_latas = quant_latas*80
valor_galoes = quant_galoes*25
valor = valor_latas + valor_galoes

print(f"Você precisará de {quant_latas} latas e {quant_galoes} galões de tinta, e valor total a ser gasto será de R${valor:.2f}.")