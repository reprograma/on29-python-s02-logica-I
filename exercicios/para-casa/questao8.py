def contar_dig(num):
    num_string = str(num)
    return len(num_string)

num = int(input("Digite um número inteiro: "))
quant_dig = contar_dig(num)
print(f"A quantidade de dígitos do número {num} é de {quant_dig}")
