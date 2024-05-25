areapintada = int(input("Qual a metragem da area a ser pintada? "))*1.1
litros = areapintada/6
latas = litros//18
restantelitros = litros%18
galao = restantelitros//3.6
if restantelitros%3.6 > 0:
    galao = galao + 1
custo = latas*80 + galao*25
print("A quantidade de latas necessarias é: ", latas )
print("A quantidade de galao necessarias é: ", galao )
print("O custo total é: ", custo)

