# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser 
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
 # comprar apenas latas de 18 litros;
 # comprar apenas galões de 3,6 litros;
 # misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
 # sempre arredonde os valores para cima, isto é, considere latas cheias.

tamanho_area = float(input("Informe o tamanho em metros quadrados: "))

litros = tamanho_area / 6
latas = litros / 18

if latas % 18 != 0:
    latas += 1
    
preco = latas * 80

galoes = litros / 3.6

if galoes % 3.6 != 0:
    galoes += 1
preco2 = galoes * 25


mistura_lata = int(litros / 18.0)
mistura_galao = int((litros - (mistura_lata * 18)) / 3.6)

if litros - (mistura_lata * 18) % 3.6 != 0:
    mistura_galao += 1

print('Apenas latas de 18 litros: %d' % latas, 'preço: %d' % preco)
print('Apenas galões de 3.6 litros: %d' % galoes, 'preço: %d' % preco2)
print('Mistura: %d latas e %d galoes = %.2f' % (
    mistura_lata, mistura_galao, ((mistura_lata * 80) + (mistura_galao * 25))))
