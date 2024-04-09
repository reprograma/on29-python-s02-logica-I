from math import ceil

tamanhoArea = float(input("Qual o tamanho em metros quadrados da área que deseja pintar? "))
quantidadeLatas = tamanhoArea / 3
totalLatas = ceil(quantidadeLatas / 18)
valorTotal = totalLatas * 80

print(f"Para pintar a sua área de {tamanhoArea}m² você vai precisar de {totalLatas:.2f} lata (s) de tinta, e o valor total será de R${valorTotal:.2f}")










