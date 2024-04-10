def argumento():
    a = float(input("Digite um número: "))
    if a > 0:
        return "P"
    else:
        return "N"

resultado = argumento()
print("Resultado:", resultado)
