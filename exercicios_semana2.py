import math

# 16
valor_area = input("Insira (em metros quadrados) o tamanho da área a ser pintada")

print (f"A área a ser pintada é: {valor_area} metros")

quantidade_litros = float(valor_area)/3
quantidade_latas = math.ceil(quantidade_litros/18)
preco = quantidade_latas * 80


print (f"Quantidade de latas necessárias: {quantidade_latas}")
print (f"Preço Tota: {preco} reais")

# 17

lata = 18
galao = 3.6

valor_area2 = input("Insira (em metros quadrados) o tamanho da área a ser pintada")

print (f"A área a ser pintada é: {valor_area2} metros")

quantidade_litros2 = (float(valor_area2)/6) + 0.1
print (quantidade_litros2)

quantidade_latas = math.ceil(quantidade_litros2/lata)
quantidade_galoes = math.ceil(quantidade_litros2/galao)

litros_inte = math.floor (quantidade_litros2/lata)
resto_latas = quantidade_litros2 -litros_inte * lata
print (resto_latas)
galoes_restl = math.ceil(resto_latas /galao)



preco_latas = quantidade_latas * 80
preco_galoes = quantidade_galoes * 25
preco_galoeslatas = (litros_inte * 80) + (galoes_restl *25)

print ("Temos 3 opções de compra:")

print (f"Opção 1: LATAS\n Quantidade necessárias: {quantidade_latas} latas.")
print (f"Preço Tota: {preco_latas} reais")

print (f"Opção 1: GALÕES\n Quantidade necessárias: {quantidade_galoes} galões.")
print (f"Preço Tota: {preco_galoes} reais")

print (f"Opção 3: GALÕES + LATAS\n Quantidade necessárias: {galoes_restl} galões e {litros_inte} latas.")
print (f"Preço Tota: {preco_galoeslatas} reais")

# 3

def somar(a,b,c):
    soma = a+b+c
    return soma 

print (somar(3,5,6))
 



