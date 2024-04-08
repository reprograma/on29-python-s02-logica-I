# Atividade - Semana 2

# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


# Interatividade com o usuário

menu = "**********************************************************"
menu += "\n*                                                        *"
menu += "\n*          Bem vinde a nossa loja de tintas!             *"
menu += "\n*                                                        *"
menu += "\n**********************************************************"
menu += "\n*                                                        *"
menu += "\n* Cobertura da tinta: 1L para cada 3m²                   *"
menu += "\n* Disponibilidade: Latas de 18L, custando R$ 80,00       *"
menu += "\n*                                                        *"
menu += "\n**********************************************************"
menu += "\n*                                                        *"

print(menu)

tamanho_area = eval(input("* Qual o tamanho da área a ser pintada (em m²)? "))

menu2 = "*                                                        *"
menu2 += "\n**********************************************************"
menu2 += "\n*                                                        *"

print(menu2)


# Define a cobertura da tinta em metros quadrados por litro
cobertura_por_litro = 3

# Calcula a quantidade de litros necessários
litros_necessarios = tamanho_area / cobertura_por_litro

# Calcula o número de latas de tinta necessárias, arredondando para cima
latas_necessarias = int(litros_necessarios / 18)
if litros_necessarios % 18 != 0:
    latas_necessarias += 1

# Calcula o preço total das latas de tinta
preco_total = latas_necessarias * 80

# Exibe a quantidade de latas de tinta necessárias e o preço total

menu3 = f"* Você precisará de {latas_necessarias} latas de tinta.                   *"
menu3 += f"\n* O preço total será de R$ {preco_total:.2f}.                      *"
menu3 += "\n*                                                        *"
menu3 += "\n**********************************************************"

print(menu3)