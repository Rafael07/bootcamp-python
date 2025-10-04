# Exercícios de Listas e Dicionários
# 1 Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

# lista: list = [print(numero**2) for numero in range(1,11)]

# 2 Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

# languages: list = ["Python", "Java", "C++", "JavaScript"]
# languages.remove('C++')
# languages.append('Ruby')
# print(languages)

# 3 Crie um dicionário para armazenar informações de um livro, incluindo título, autor 
# e ano de publicação. Imprima cada informação.


# def inserir_livros(titulo: str, autor: str, ano_publicacao: int) -> dict:
#     livros_dict['titulo'] = titulo
#     livros_dict['autor'] = autor
#     livros_dict['ano_publicacao'] = ano_publicacao
#     return livros_dict

# def imprimir_livros(dicionario: dict):
#     print(f'Título do livro: {dicionario['titulo']}')
#     print(f'Autor do livro: {dicionario['autor']}')
#     print(f'Ano de publicação: {dicionario['ano_publicacao']}')

# livros_dict: dict = {}

# titulo: str = input('Insira o título do livro: ')
# autor: str = input('Insira o autor do livro: ')
# ano: int = int(input("Insira o ano de publivação do livro: "))
# print("")
# inserir_livros(titulo, autor, ano)
# imprimir_livros(livros_dict)


# 4 Escreva um programa que conta o número de ocorrências de cada 
# caractere em uma string usando um dicionário.

# def contagem_ocorrencias(frase: str) -> dict:
#     dicionario: dict = {}
#     frase = frase.lower().strip()
#     for caracter in frase:
#         #if caracter in string.punctuation or caracter == '':
#         if not caracter.isalpha():
#             pass
#         else:
#             dicionario[caracter] = dicionario.get(caracter, 0) + 1
#     return dicionario

# #caracter_especiais = string.punctuation
# frase: str = input('Escreva o que quiser: ')
# print(contagem_ocorrencias(frase))

# 5 Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65},
# calcule o preço total da lista de compras.

lista: list = ["maçã", "banana", "cereja"]
dicionario: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

# total: float = 0
# for item in lista:
#     total += dicionario[item]

total = sum(dicionario[item] for item in lista)
print(f'O preço total da lista de compras é {total:.2f}')