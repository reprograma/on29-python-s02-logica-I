#ATIVIDADE 3 - FUNÇÕES

#CRIAR UMA FUNÇÃO COM 3 PARAMETROS QUE ENTREGUE A SOMA DELES

def soma(a, b, c):
    print('-' * 30)
    valor_final = a + b + c
    print(valor_final)
    print('-' * 30)


soma(2, 4, 5)




#-------------------------------------------------------------------------------------------------
#exercicio 17
conteudo_da_lata_em_litros = 18
metro_coberto_cada_um_litro = 6
valor_cada_lata = 80

conteudo_galoes_em_litros = 3.6





def titulos(texto):
    print('-' * 30)
    print(texto)
    print('-' * 30)


titulos('EXERCICIO 17')
titulos('A SEGUNDA LOJA DE TINTAS DA BLANCA')


area_a_pintar = int(input('Insira aqui a quantidade de metros quadrados da area a ser pintada: '))


numero_latas_necessarias = (conteudo_da_lata_em_litros * metro_coberto_cada_um_litro) / area_a_pintar

numero_galoes_necessarios = (conteudo_galoes_em_litros * metro_coberto_cada_um_litro) / area_a_pintar

 
valor_final_latas = numero_latas_necessarias * valor_cada_lata

valor_final_galoes = numero_galoes_necessarios * 25

print('para cobrir ', area_a_pintar, 'metros será necessário o uso de ', numero_latas_necessarias, 'latas, que ficarão em um total de R$ ', valor_final_latas)

print('È possivel também a compra de galões de 3,6 litros. Nesse caso serão necessários ', numero_galoes_necessarios, 'galões, que ficarão em um total de R$ ', valor_final_galoes)






#----------------------_____-----------------------------------------------------
#Exercicio 16

def titulos(texto):
    print('-' * 30)
    print(texto)
    print('-' * 30)


titulos('EXERCICIO 16')
titulos('LOJA DE TINTAS DA BLANCA')



area_a_pintar = int(input('Insira aqui a quantidade de metros quadrados da area a ser pintada: '))

numero_latas_necessarias = area_a_pintar / 54

 
valor_final_latas = numero_latas_necessarias * 80


print('Para ', area_a_pintar, 'metros será necessário o uso de ', numero_latas_necessarias,'latas, que vão ficar em um total de R$ ', valor_final_latas)