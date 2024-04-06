def calculo_recuperação(nota_regular, nota_recuperação):
    media_final = (nota_regular + nota_recuperação)/2
    print(media_final)


def calculo_media_ponderada(nota1, peso1, nota2, peso2, nota3, peso3):
    media =  (nota1 * peso1 + nota2 *peso2 + nota3 * peso3)/(peso1 + peso2 + peso3)
    return media

nota1, nota2, nota3 = 10, 10, 1
peso1, peso2, peso3 = 1, 3.5, 5.5
nota_recuperação = 7
media_regular = calculo_media_ponderada(nota1, peso1, nota2, peso2, nota3, peso3)
calculo_recuperação = calculo_recuperação(media_regular, nota_recuperação)

