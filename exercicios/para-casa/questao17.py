# Questão 17

area_total = float(input("Informe a àrea total que vc deseja pintar em metros quadrados:"))
area_litro = 6
galao = 3.6
lata = 18
valor_lata = 80
valor_galao = 25
valor_total = (area_total * valor_lata) / (lata * area_litro)
valor_total_g = (area_total * valor_galao) / (galao * area_litro)
total_latas = area_total / (area_litro * lata)
total_galao = area_total / (area_litro * galao)
area_min = round(129.6 * 1.1, -1) # aqui tentei definir uma area minima na qual seria possivel misturar latas e galões,
# e coloquei a função arrendondar.


def comprar_lata():
  resultado = comprar_lata(total_latas, valor_total)
  print(resultado)

def comprar_galao():
  resultado2 = comprar_galao(valor_total_g, total_galao)
print (resultado2)
  
def juntar():
  if area_total >= area_min:
    total_junto = valor_total + valor_total_g
  resultado3 = juntar(total_junto)
  print (resultado)

    