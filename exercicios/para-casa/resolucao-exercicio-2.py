# Relosução exercício da aula 02

# exercício 3 função
import math


def info_aluna(nome, idade, cidade):
    info = nome + ", " + idade + " anos, " + cidade
    return info


nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")

info_completa = info_aluna(nome, idade, cidade)
print("Informações da aluna: " + info_completa)

# exercício 16
area = float(
    input("Digite o tamanho da área em metros quadrados a ser pintada: "))
litro = area / 3
lata = math.ceil(litro/18)
custo = (lata) * 80
tinta = ("Para seu orçamento será necessário: " + str(
    lata) + " litros de tinta. Com valor final de: R$" + str(custo))
print(tinta)

# exercício 17
area2 = float(input("Digite o tamanho da área a ser pintada: "))
folga = area2 * 1.1
litro2 = folga / 6
lata2 = math.ceil(litro2/18)
custolata = (lata2) * 80
# calculo galões
galao = math.ceil(litro2/3.6)
custogalao = (lata2) * 25

# comprar apenas latas de 18 litros;
orca_lata = ("Para seu orçamento em latas, será necessário: " +
             str(lata2) + " latas, com valor total de: R$" + str(custolata))
print(orca_lata)
# comprar apenas galões de 3,6 litros;
orca_galao = ("Para seu orçamento em galões será necessário: " +
              str(galao) + " galões, com valor total de: R$" + str(custogalao))
print(orca_galao)
# misturar latas e galões, desperdício de tinta seja menor.
lata_mistura = math.floor(litro2 / 18)
sobra = litro2 % 18
galao_mistura = math.ceil(sobra / 3.6)
custo_mistura = lata_mistura * 80 + galao_mistura * 25
orca_mistura = ("Para seu orçamento mais econômico e com  menor desperdício, temos: " +
                str(lata_mistura) + " latas, mais " + str(galao_mistura) + " galões, com valor total de: R$" + str(custo_mistura))
print(orca_mistura)
