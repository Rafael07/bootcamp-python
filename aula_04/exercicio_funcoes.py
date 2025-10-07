# # Implementação do algoritmo de ordenação por seleção
# lista = [64, 34, 25, 12, 22, 11, 90]

# for i in range(len(lista)):
#     for j in range(i+1, len(lista)):
#         if lista[i] > lista[j]:
#             lista[i], lista[j] = lista[j], lista[i]

# # Ordenando a lista
# print("Lista ordenada com função personalizada:", lista)

# # Ordenando a lista com sort()
# lista_exemplo = [64, 34, 25, 12, 22, 11, 90]
# lista_exemplo.sort()
# print("Lista ordenada com método built-in:", lista_exemplo)



# Exercícios de Funções
# 1. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
# ----------------------------------------------------------------------------------------------

# def somar_numeros_de_lista(lista: list) -> int:
#     soma: int = 0
#     for numero in lista:
#         soma += numero
#     return soma

# import random

# lista_numeros = [random.randint(1,100) for _ in range(10) ]
# print(f'Lista de números de entrada: {lista_numeros}')

# soma_da_lista = somar_numeros_de_lista(lista_numeros)
# print(f'Soma dos números da lista: {soma_da_lista}')

# 2. Crie uma função que receba um número como argumento e retorne True se o número for primo
#  e False caso contrário.
# ----------------------------------------------------------------------------------------------

# def verificar_numero_primo(numero: int) -> bool:
#     num_divisores = 0
#     for num in range(1,numero+1):
#         resultado = numero % num
#         if resultado == 0:
#             num_divisores += 1
#     if num_divisores == 2:
#         return True
#     else:
#         return False
    
# numero = int(input("Insira um numero: "))
# resposta = verificar_numero_primo(numero)
# if resposta == True:
#     print(f'O número {numero} é primo.')
# else:
#     print(f'O número {numero} não é primo.')

# 3. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
# ----------------------------------------------------------------------------------------------

def string_reversa(uma_string: str) -> str:

    return ''.join(reversed(uma_string))

nova_string = input("Insira uma string: ")
print(string_reversa(nova_string))

# 4. Implemente uma função que receba dois argumentos: uma lista de números e um número. 
# A função deve retornar todas as combinações de pares na lista que somem ao número dado.
# ----------------------------------------------------------------------------------------------

# 5. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
# ----------------------------------------------------------------------------------------------