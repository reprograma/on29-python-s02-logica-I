def soma_tres_numeros(a, b, c):
    return a + b + c

def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

    resultado = soma_tres_numeros(num1, num2, num3)
    print(f"A soma dos três números é: {resultado}")

# Chamando a função principal
if __name__ == "__main__":
    main()