area = float(input("Informe o tamanho da area a ser pintada em metros quadrados: "))
litros_necessarios = area / 3
quantidade_latas = int(litros_necessarios / 18)

if litros_necessarios % 18 != 0:
    quantidade_latas += 1

preco_total = quantidade_latas * 80.00

print(f"Quantidade de latas de tinta necessarias: {quantidade_latas}")
print(f"Preço total: R$ {preco_total:.2f}")