    # abaixo está minha resposta do número 16
    # bom dia!

metros_quadrados_total = input("Quantidade de metros quadrados da área pintada: ") 
quantidade_metros_por_litro = 3
preco_lata = 80
litros_por_lata = 18
metros_pintados_lata = quantidade_metros_por_litro * litros_por_lata
quantidade_de_latas = int(metros_quadrados_total) / metros_pintados_lata 
preco_total = preco_lata * quantidade_de_latas  
print("O preço a ser pago e a quantidade de latas compradas: " +  str(preco_total )  +  " e "  +  str(quantidade_de_latas ))
