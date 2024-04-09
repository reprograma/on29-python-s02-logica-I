#Questão 3 - Fazer um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos

#Criando um programa para cálculo do perímetro de um triângulo

print("\nPara obtenção do perímetro de um triângulo qualquer, insira abaixo o comprimento de cada um dos seus lados:")

lado1 = float(input("\nComprimento do lado 1: "))
lado2 = float(input("Comprimento do lado 2: "))
lado3 = float(input("Comprimento do lado 3: "))

def perimetro_triangulo(lado1, lado2, lado3):
    soma = lado1 + lado2 + lado3
    return soma

perimetro_triangulo(lado1, lado2, lado3)

resultado_perimetro_triangulo = round(perimetro_triangulo(lado1, lado2, lado3), 2)

print(f"\nO perímetro do triângulo contendo os lados informados é: {resultado_perimetro_triangulo}")