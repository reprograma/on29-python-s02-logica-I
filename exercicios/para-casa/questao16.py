# Questão 16

area_total = float(input("Informe a àrea total que vc deseja pintar em metros quadrados:"))
area_litro = 3
lata_litro = 18
valor_lata = 80
valor_total = (area_total * valor_lata) / (lata_litro * area_litro)
total_latas = area_total / (area_litro * lata_litro)

print("\n Para a área informada, o valor total é de R$ {:.2f}".format(valor_total))
print(f"\n O total de latas necessárias para pintar a área de {area_total:,.2f} m² é de {total_latas:,.2f} latas")