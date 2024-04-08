# Atividade - Semana 2

# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

# Definindo a função para a soma dos três argumentos

def calcular_soma():
    print("*----------------------------------------------------------*")
    print("*                    Vamos somar?                          *")
    print("*----------------------------------------------------------*")

    arg_1 = eval(input("* Insira o primeiro número a ser somado: "))
    arg_2 = eval(input("* Insira o segundo número a ser somado: "))
    arg_3 = eval(input("* Insira o terceiro número a ser somado: "))

    soma = (arg_1) + (arg_2) + (arg_3)

    print("*----------------------------------------------------------*")
    print(f"* A soma dos três números é dada por: {soma}.                  *")
    print("*----------------------------------------------------------*")

calcular_soma()
