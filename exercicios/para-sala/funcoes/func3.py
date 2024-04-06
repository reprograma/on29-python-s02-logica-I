def calculo_media_ponderada(nota1, peso1, nota2, peso2, nota3, peso3):
    media =  (nota1 * peso1 + nota2 *peso2 + nota3 * peso3)/(peso1 + peso2 + peso3)
    print(media)

nota1, nota2, nota3 = 10, 10, 1
peso1, peso2, peso3 = 1, 3.5, 5.5
calculo_media_ponderada(nota1, peso1, nota2, peso2, nota3, peso3)

