import math

# Função para arredondar para cima
def arredonda_para_cima(numero):
    inteiro = int(numero)
    return inteiro + (1 if numero - inteiro > 0 else 0)

# Função para calcular a quantidade de tinta necessária
def calcula_litros_necessarios(area):
    return area / 6 * 1.1  # 10% de folga

# Função para calcular a quantidade de latas e o preço para comprar apenas latas de 18 litros
def comprar_apenas_latas(litros_necessarios):
    quantidade_latas = arredonda_para_cima(litros_necessarios / 18)
    preco_total = quantidade_latas * 80.00
    return quantidade_latas, preco_total

# Função para calcular a quantidade de galões e o preço para comprar apenas galões de 3,6 litros
def comprar_apenas_galoes(litros_necessarios):
    quantidade_galoes = arredonda_para_cima(litros_necessarios / 3.6)
    preco_total = quantidade_galoes * 25.00
    return quantidade_galoes, preco_total

# Função para calcular a quantidade de latas e galões e o preço para misturar latas e galões
def misturar_latas_galoes(litros_necessarios):
    quantidade_latas = int(litros_necessarios // 18)
    litros_restantes = litros_necessarios % 18
    quantidade_galoes = arredonda_para_cima(litros_restantes / 3.6)
    
    preco_latas = quantidade_latas * 80.00
    preco_galoes = quantidade_galoes * 25.00
    preco_total = preco_latas + preco_galoes
    
    return quantidade_latas, quantidade_galoes, preco_total

# Solicitando ao usuário o tamanho da área a ser pintada
area = float(input("Informe o tamanho da area a ser pintada em metros quadrados: "))

# Calculando a quantidade de tinta necessária
litros_necessarios = calcula_litros_necessarios(area)

# Comprar apenas latas de 18 litros
quantidade_latas, preco_latas = comprar_apenas_latas(litros_necessarios)

# Comprar apenas galões de 3,6 litros
quantidade_galoes, preco_galoes = comprar_apenas_galoes(litros_necessarios)

# Misturar latas e galões
quantidade_latas_mistura, quantidade_galoes_mistura, preco_total_mistura = misturar_latas_galoes(litros_necessarios)

# Exibindo os resultados
print(f"Comprar apenas latas de 18 litros:")
print(f"Quantidade de latas: {quantidade_latas}")
print(f"Preço total: R$ {preco_latas:.2f}\n")

print(f"Comprar apenas galoes de 3,6 litros:")
print(f"Quantidade de galoes: {quantidade_galoes}")
print(f"Preço total: R$ {preco_galoes:.2f}\n")

print(f"Misturar latas e galoes:")
print(f"Quantidade de latas: {quantidade_latas_mistura}")
print(f"Quantidade de galoes: {quantidade_galoes_mistura}")
print(f"Preço total: R$ {preco_total_mistura:.2f}")