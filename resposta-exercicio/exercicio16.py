# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de
# latas de tinta a serem compradas e o preço total

cobertura_da_tinta = 3

tamanho_area = float(input("Informe o tamanho em metros quadrados: "))

litros = tamanho_area/cobertura_da_tinta
unidade_lata = 18
preco_lata = 80.00

latas_int = int(litros/unidade_lata)

if (litros % unidade_lata != 0):
    unidade_lata += 1

valor_total = latas_int * preco_lata

print("A quantidade necessária de latas de tintas é de: ", latas_int)
print("A quantidade de litros de tinta é de: ", litros)
print("O valor total da compra é de R$: ", valor_total)