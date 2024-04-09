import math

print('Orçamento - Loja PoneiTintas')
tamanho_da_area = input('Digite aqui, em m², o tamanho da área a ser pintada: ')
rendimento_por_litro = 3
quantidade_por_lata = 18
valor_lata = 80
area_por_lata = rendimento_por_litro * quantidade_por_lata
quantidade_total_latas = int(tamanho_da_area) / area_por_lata
valor_total = (math.ceil(quantidade_total_latas)) * valor_lata
print('Quantidade necessária de latas: ', math.ceil(quantidade_total_latas))
print('Valor total da compra: R$', valor_total)
print('Entre em contato com nossos vendedores para conhecer nossas formas de pagamento!')
