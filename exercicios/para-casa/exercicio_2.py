import math

print('Orçamento - Loja PoneiTintas')
tamanho_da_area = float(input('Digite aqui, em m², o tamanho da área a ser pintada: '))
rendimento_litro = 6
quantidade_lata = 18
valor_lata = 80
quantidade_galao = 3.6
valor_galao = 25

area_lata = rendimento_litro * quantidade_lata
quantidade_total_latas = tamanho_da_area / area_lata
total_lata = math.ceil(quantidade_total_latas) * valor_lata
print('OPÇÃO 1: COMPRANDO APENAS LATAS')
print('Considerando apenas latas, você deverá comprar ', math.ceil(quantidade_total_latas), 'unidades.')
print('Valor total - apenas latas: R$', total_lata)

area_galao = rendimento_litro * quantidade_galao
quantidade_total_galoes = tamanho_da_area / area_galao
total_galao = math.ceil(quantidade_total_galoes) * valor_galao
print('OPÇÃO 2: COMPRANDO APENAS GALÕES')
print('Considerando apenas galões, você deverá comprar ', math.ceil(quantidade_total_galoes), 'unidades.')
print('Valor total - apenas galões: R$', total_galao)


print('OPÇÃO 3: COMPRANDO LATAS E GALÕES')
tamanho_da_area_mistura = tamanho_da_area * 1.1
mistura_lata = tamanho_da_area_mistura//area_lata
print('Quantidade de latas na mistura', math.ceil(mistura_lata))
mistura_galao = (tamanho_da_area_mistura % area_lata)/area_galao
print('Quantidade de galões na mistura', math.ceil(mistura_galao))
total_mistura = (math.ceil(mistura_lata) * valor_lata) + (math.ceil(mistura_galao) * valor_galao)
print('Valor total - latas e galões: R$', round(total_mistura, 2))

print('Entre em contato com nossos vendedores para conhecer nossas formas de pagamento!')

