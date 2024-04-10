# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(variavel1, variavel2, variavel3):
    soma = variavel1 + variavel2 + variavel3
    return soma

variavel1 = int(input("Informe o primeiro número: "))
variavel2 = int(input("Informe o segundo número: "))
variavel3 = int(input("Informe o terceiro número: "))

print("O valor da soma é: ", soma(variavel1, variavel2, variavel3))