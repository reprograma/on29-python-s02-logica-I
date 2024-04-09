import math

area = float(input("Insira a quantidade, em metros quadrados, de área a ser pintada: "))
quant_galoes = math.ceil(area/21.6)
valor = quant_galoes*25

print(f"Você precisará de {quant_galoes} galões de tinta, e valor total a ser gasto será de R${valor:.2f}.")