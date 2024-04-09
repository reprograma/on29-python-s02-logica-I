numeroUm = int(input("Digite um número: "))
numeroDois = int(input("Digite um segundo número: "))
numeroTres = int(input("Digite o terceiro número: "))

def calculo():
    soma = numeroUm + numeroDois + numeroTres
    print(f"A soma dos números é {soma}")
    return soma

calculo()
