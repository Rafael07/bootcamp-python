# Exercícios
# Aqui estão cinco exercícios que envolvem TypeError, verificação de tipo (type check),
# o uso de try-except para tratamento de exceções e a utilização da
# estrutura condicional if.
# Esses exercícios aumentam progressivamente em dificuldade e abordam situações
# práticas onde você pode aplicar esses conceitos.

# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit.
# O programa deve solicitar ao usuário a temperatura em Celsius e,
# utilizando try-except, garantir que a entrada seja numérica,
# tratando qualquer ValueError.
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

# def temperature_conversor(C):
#     F =  (C * 1.8) + 32
#     return F
# try:
#     temp = float(input("Insira uma temperatura em Celsius: "))
#     F = temperature_conversor(temp)
#     print(f"A temperatura {temp}°C equivale a {F}°Farenheit.")
# except ValueError as e:
#     print(e)


# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo
# (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações).
# Utilize try-except para garantir que a entrada seja uma string.
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.

# def palindrome(palavra):
#     if palavra == palavra[::-1]:
#         print("Is a palindrome!")
#     else:
#         print("It is not a palindrome!")

# palavra = input("Insira uma palavra: ")
# palavra = palavra.strip().lower()
# try:
#     if not isinstance(palavra, str):
#         raise TypeError("A entrada não foi uma string.")
#     if not palavra.isalpha():
#         raise TypeError("A entrada deve conter apenas letras!")
#     palindrome(palavra)
# except TypeError as e:
#     print(f"Erro: {e}")

# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas
# e um operador (+, -, *, /) do usuário.
# Use try-except para lidar com divisões por zero e entradas não numéricas.
# Utilize if-elif-else para realizar a operação matemática
# baseada no operador fornecido.
# Imprima o resultado ou uma mensagem de erro apropriada.

# def soma(num01, num02):
#     return num01 + num02
# def subtracao(num01, num02):
#     return num01 - num02
# def mult(num01, num02):
#     return num01 * num02
# def div(num01, num02):
#     return num01 / num02

# print("-"*5 + " Calculadora Simples " + "-"*5)

# operacoes = {
#     "+": soma,
#     "-": subtracao,
#     "*": mult,
#     "/": div
# }

# try:
#     num01 = int(input("Insira um número: "))
#     num02 = int(input("Insira outro número: "))
#     operador = input("Insira um operador +, -, *, /: ")

#     if operador not in operacoes:
#         raise ValueError("Operador inválido.")

#     resultado = operacoes[operador](num01, num02)
#     print(resultado)

# except ValueError as e:
#     if "invalid literal" in str(e):
#         print(f"Erro: apenas números inteiros são aceitos.")
#     elif "Operador inválido." in str(e):
#         print("Erro: o operador informado não é válido. Confira a lista fornecida.")
#     else:
#         print(f"Erro inesperado: {e}")
# except ZeroDivisionError:
#     print("Erro: divisão por zero não é permitida.")


# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número.
# Utilize try-except para assegurar que a entrada seja numérica
# e utilize if-elif-else para classificar o número
# como "positivo", "negativo" ou "zero".
# Adicionalmente, identifique se o número é "par" ou "ímpar".

# def par_ou_impar(num):
#     if num % 2 == 0:
#         return "Par!"
#     else:
#         return "Ímpar!"

# try:
#     num = int(input("Insira um número: "))

#     if num > 0:
#         print("positivo")
#     elif num < 0:
#         print("negativo")
#     else:
#         print("zero")

#     print(par_ou_impar(num))

# except ValueError:
#     print("O programa aceita apenas números!")


# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula.
# O programa deve converter a string de entrada em uma lista de números inteiros.
# Utilize try-except para tratar a conversão de cada número e validar que cada
# elemento da lista convertida é um inteiro.
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro.
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

# lista = input("Insira uma lista de números separados por virgula: ")

# lista = lista.split(',')
# numbers = []
# try:
#     for item in lista:
#         item = item.strip()
#         if item.isdigit():
#             numbers.append(int(item))
#     print(f"Lista de inteiros: {numbers}")
# except:
#     print('Erro!')

# Exercicio de treino
# Criar uma aplicação que recebe alunos e atribui notas a eles, ao fim da atribuição
#  das notas, calcular media e indica se o aluno foi aprovado ou reprovado.
# O resultado pode ser consultado na lista de aprovados e noutra de reprovados.
# Foque no uso de listas, não precisar tratar erros e validar os dados.

import pandas as pd

alunos = []
notas = []
situacao = []


def adicionar_aluno() -> list:
    nome_aluno = input("Insira o nome do aluno: ")
    alunos.append(nome_aluno)
    return alunos


def adicionar_notas() -> list:
    nota01 = float(input("Insira a primeira nota: "))
    nota02 = float(input("Insira a segunda nota: "))
    nota03 = float(input("Insira a terceira nota: "))
    nota04 = float(input("Insira a quarta nota: "))
    notas.append([nota01, nota02, nota03, nota04])
    return notas


def calcular_media(notas: list):
    if len(notas) == len(alunos):
        media = (notas[-1][0] + notas[-1][1] + notas[-1][2] + notas[-1][3]) / 4
    if media >= 7:
        situacao.append("Aprovado")
    else:
        situacao.append("Reprovado")
    return media


def checar_aprovados():
    for aluno, situacao_final in zip(alunos, situacao):
        if situacao_final == "Aprovado":
            print(f"{aluno} foi aprovado")
        else:
            print(f"{aluno} foi reprovado")


def gravar_csv():
    df_notas = pd.DataFrame(notas, columns=["Nota_01", "Nota_02", "Nota_03", "Nota_04"])
    df_alunos = pd.DataFrame(alunos, columns=["Alunos"])
    df_sit = pd.DataFrame(situacao, columns=["Situação"])
    df = pd.concat([df_alunos, df_notas, df_sit], axis=1)
    df.to_csv("alunos.csv", index=False)


while True:
    print("-" * 5 + " Sistema de notas " + "-" * 5)
    print("1 - Adicionar aluno")
    print("2 - Ver situação do aluno")
    print("0 - Sair")
    opcao = int(input("Insira uma opção: "))

    if opcao == 1:
        adicionar_aluno()
        adicionar_notas()
        calcular_media(notas)
    elif opcao == 2:
        checar_aprovados()
    elif opcao == 0:
        gravar_csv()
        break
