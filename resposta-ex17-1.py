import math

area = float(input("Insira a quantidade, em metros quadrados, de área a ser pintada: "))
quant_latas = math.ceil(area/108)
valor = quant_latas*80

print(f"Você precisará de {quant_latas} latas de tinta, e valor total a ser gasto será de R${valor:.2f}.")