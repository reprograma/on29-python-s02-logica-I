# Atividade - Semana 2

"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

# Interatividade com o usuário

menu = "**********************************************************"
menu += "\n*                                                        *"
menu += "\n*          Bem vinde a nossa loja de tintas!             *"
menu += "\n*                                                        *"
menu += "\n**********************************************************"
menu += "\n*                                                        *"
menu += "\n* Cobertura da tinta: 1L para cada 6m²                   *"
menu += "\n* Disponibilidade:                                       *"
menu += "\n* - Galões de 3.6L, custando R$ 25,00                    *"
menu += "\n* - Latas de 18L, custando R$ 80,00                      *"
menu += "\n*                                                        *"
menu += "\n**********************************************************"
menu += "\n*                                                        *"

print(menu)

# Função para calcular a quantidade de tinta necessária em litros
def calcular_tinta(area):
    return area / 6

# Função para arredondar para cima
def arredondar_cima(numero):
    if numero % 1 == 0:
        return int(numero)
    return int(numero) + 1

# Função para calcular o número de latas necessárias
def calcular_latas(tinta):
    return arredondar_cima(tinta / 18)

# Função para calcular o número de galões necessários
def calcular_galoes(tinta):
    return arredondar_cima(tinta / 3.6)

# Função para calcular a combinação ideal de latas e galões
def calcular_combinacao(tinta):
    latas = int(tinta / 18)
    galoes = arredondar_cima((tinta % 18) / 3.6)
    return latas, galoes

# Função para calcular o preço total de latas
def calcular_preco_latas(latas):
    return latas * 80

# Função para calcular o preço total de galões
def calcular_preco_galoes(galoes):
    return galoes * 25

# Função para calcular o preço total da combinação
def calcular_preco_combinacao(latas, galoes):
    return latas * 80 + galoes * 25

# Função principal
def main():
    area = eval(input("* Qual o tamanho da área a ser pintada (em m²)? "))

    # Calcula a quantidade necessária de tinta
    tinta = calcular_tinta(area)

    # Calcula as opções de compra
    latas_necessarias = calcular_latas(tinta)
    galoes_necessarios = calcular_galoes(tinta)
    latas_combinacao, galoes_combinacao = calcular_combinacao(tinta)

    # Calcula os preços
    preco_latas = calcular_preco_latas(latas_necessarias)
    preco_galoes = calcular_preco_galoes(galoes_necessarios)
    preco_combinacao = calcular_preco_combinacao(latas_combinacao, galoes_combinacao)

    # Imprime os resultados

    menu1 = "*                                                        *"
    menu1 += "\n**********************************************************"
    menu1 += "\n*                                                        *"
    menu1 += "\n* Opção 1: Comprar apenas latas de 18 litros             *"
    menu1 += f"\n* Quantidade de latas necessárias: {latas_necessarias}" 
    menu1 += f"\n* Preço total: R$ {preco_latas: .2f}"
    menu1 += "\n*                                                        *"
    menu1 += "\n**********************************************************"
    
    menu2 = "*                                                        *"
    menu2 += "\n* Opção 2: Comprar apenas galões de 3.6 litros           *"
    menu2 += f"\n* Quantidade de galões necessários: {galoes_necessarios}" 
    menu2 += f"\n* Preço total: R$ {preco_galoes: .2f}"
    menu2 += "\n*                                                        *"
    menu2 += "\n**********************************************************"

    menu3 = "*                                                        *"
    menu3 += "\n* Opção 3: Misturar latas e galões                       *"
    menu3 += f"\n* Quantidade de latas necessárias: {latas_combinacao}" 
    menu3 += f"\n* Quantidade de galões necessários: {galoes_combinacao}" 
    menu3 += f"\n* Preço total: R$ {preco_combinacao: .2f}"
    menu3 += "\n*                                                        *"
    menu3 += "\n**********************************************************"

    print(menu1)
    print(menu2)
    print(menu3)

# Chamada da função principal
main()

