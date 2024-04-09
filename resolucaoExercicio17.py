from math import ceil 

tamanhoArea = float(input("Qual o tamanho da área em metros quadrados que deseja pintar? "))
margemFolga = (tamanhoArea * 10) / 100
totalArea = tamanhoArea + margemFolga 
quantidadeLitros = ceil(totalArea / 6) 
print(f"Você precisa de {quantidadeLitros}litros para pintar a sua área de {totalArea}m² aproximadamente.")

capacidadeLatas = 18
totalLatas = ceil(quantidadeLitros / 18)
valorTotalLatas = totalLatas * 80 

capacidadeGaloes = 3.6
totalGaloes = ceil(quantidadeLitros / 3.6)
valorTotalGaloes = totalGaloes * 25



print(f"Para pintar a sua área de {totalArea}m² com Galões de {capacidadeGaloes}l, você precisará de {totalGaloes} galões e o total será de R${valorTotalGaloes}.")
print(f"Para pintar a sua área de {totalArea}m² com Latas de {capacidadeLatas}l, você precisará de {totalLatas} latas e o total será de R$ {valorTotalLatas}.")






