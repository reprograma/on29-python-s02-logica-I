#exercicio3.py

#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def calc_soma(num1, num2, num3):
  return num1, num2, num3
num1 = int(input(f"Digite o argumento1: "))
num2 = int(input(f"Digite o argumento2: "))
num3 = int(input(f"Digite o argumento3: "))

resultado = (num1 + num2 + num3)
print("A soma dos três números é:", resultado)