# Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# celsius = float(input("Informe a temperatura em Celsius que deseja converter: "))
# farenheit = (1.8 * celsius) + 32
# print(f"{celsius}° Celsius equivalem a {farenheit}° Farenheit.")

# Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# import numpy as np

# raio = float(input("Informe o raio do círculo: "))
# area = np.pi * raio**2

# print(f"A área do círculo é: {area:.2f}")

# Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário 
# e retorne o resultado da operação AND entre elas.

# expression01 = (input("Insira um bool: ")).strip().lower() == "true"

# expression02 = (input("Insira um bool: ")).strip().lower() == "true"

# result = expression01 and expression02
# print(f"O resultado é {result}.")
# print(type(expression01))
# print(type(expression02))

# Crie um programa que receba dois valores booleanos do usuário
#  e retorne o resultado da operação OR.

# expression01 = (input("Insira um bool: ")).strip().lower() == "true"

# expression02 = (input("Insira um bool: ")).strip().lower() == "true"

# result = expression01 or expression02
# print(f"O resultado é {result}.")

# Desenvolva um programa que peça ao usuário para inserir
#  um valor booleano e, em seguida, inverta esse valor.

# valor = input("Digite True ou False: ")
# if valor == "True":
#     print(False)
# else:
#     print(True)

num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))

if num1 == num2:
    print(f"Os números {num1} e {num2} são iguais.")
else:
    print(f"Os números {num1} e {num2} são diferentes.")