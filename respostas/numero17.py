    # minha resposta para o numero17
    # boa tarde!
metros_quadrados_area_pintada = input("Insira o tamanho em metros quadrados: ")
cobertura_metro_por_litro = 6
litros_lata = 18
preco_por_lata = 80
metros_por_lata = 108
litros_galao = 3.6
preco_galao = 25

    # primeira situação
    # apenas latas de 18 litros
texto = "Comprando apenas latas de 18 litros: "

quantidade_de_latas = int(metros_quadrados_area_pintada) / litros_lata
preco_latas = preco_por_lata * quantidade_de_latas
print("A quantidade de latas compradas e o preço total delas é de: " + str(quantidade_de_latas) + " latas e " + str(preco_latas) + " reais ")

    # segunda situação
    # apenas galões de 3,6 litros
texto = "Comprando apenas galões de 3,6 litros: "
quantidade_galoes_comprados = int(metros_quadrados_area_pintada) / litros_galao
preco_galoes = preco_galao * quantidade_galoes_comprados
print ("A quantidade de galões comprados e o preço total deles é de: " + str(quantidade_galoes_comprados) + " galões e " + str(preco_galoes) + " reais ")


    #terceira situação
    # misturando latas e galões
texto = "Misturando latas e galões"
    # Não consegui responder pela falta de tempo do final do dia.
