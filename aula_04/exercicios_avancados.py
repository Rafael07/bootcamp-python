# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.

# import random

# # Lista base com 10 e-mails únicos
# emails_base = [
#     "joao.silva@email.com",
#     "maria.lima@email.com",
#     "pedro.alves@email.com",
#     "ana.costa@email.com",
#     "lucas.martins@email.com",
#     "julia.rocha@email.com",
#     "carlos.souza@email.com",
#     "fernanda.pereira@email.com",
#     "bruno.oliveira@email.com",
#     "amanda.ribeiro@email.com"
# ]

# # Gerar lista com 50 e-mails, incluindo duplicatas
# emails_duplicados = [random.choice(emails_base) for _ in range(50)]

# emails_unicos = list(set(emails_duplicados))
# for index, item in enumerate(emails_unicos):
#     print(f'{index + 1}: {item}')


# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

# import random

# lista_idades = [random.randint(1, 100) for _ in range(1, 100)]

# lista_maiores = [idade for idade in lista_idades if idade >= 18]
# print(lista_maiores)

# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

# pessoas = [
#     {"nome": "João", "idade": 34},
#     {"nome": "Maria", "idade": 28},
#     {"nome": "Pedro", "idade": 45},
#     {"nome": "Ana", "idade": 19},
#     {"nome": "Lucas", "idade": 52},
#     {"nome": "Júlia", "idade": 23},
#     {"nome": "Carlos", "idade": 61},
#     {"nome": "Fernanda", "idade": 37},
#     {"nome": "Bruno", "idade": 40},
#     {"nome": "Amanda", "idade": 26},
#     {"nome": "Rafael", "idade": 33},
#     {"nome": "Beatriz", "idade": 21},
#     {"nome": "Rodrigo", "idade": 48},
#     {"nome": "Larissa", "idade": 30},
#     {"nome": "Vinícius", "idade": 55}
# ]

# pessoas.sort(key=(lambda pessoa: pessoa["nome"] ))
# print(pessoas)

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.

# numeros = [10, 40, 30, 20, 80, 50, 90, 60]
# media = sum(numeros) / len(numeros)
# print(media)

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

# valores = list(range(1,30))
# even = []
# odds = []

# for num in valores:
#     if num % 2 == 0: 
#         odds.append(num)
#     else: 
#         even.append(num)

# odds = list(filter(lambda x: x % 2==0, valores))
# even = list(filter(lambda x: x % 2!=0, valores))

# print(even)
# print(odds)

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

produtos: list = [
    {
        "id": 1,
        "nome": "Notebook Dell Inspiron",
        "categoria": "Eletrônicos",
        "preco": 3899.90,
        "estoque": 12
    },
    {
        "id": 2,
        "nome": "Smartphone Samsung Galaxy S23",
        "categoria": "Celulares",
        "preco": 4999.00,
        "estoque": 8
    },
    {
        "id": 3,
        "nome": "Fone de Ouvido Bluetooth JBL",
        "categoria": "Acessórios",
        "preco": 349.99,
        "estoque": 25
    },
    {
        "id": 4,
        "nome": "Cadeira Gamer ThunderX3",
        "categoria": "Móveis",
        "preco": 1299.90,
        "estoque": 5
    },
    {
        "id": 5,
        "nome": "Monitor LG UltraWide 29''",
        "categoria": "Eletrônicos",
        "preco": 1599.00,
        "estoque": 7
    }
]

def atualizar_preco(id: int, preco: float):
    for produto in produtos:
        if produto["id"] == id:
            produto["preco"] = preco
    return True

id_produto = int(input('Insira o ID do produto: '))
novo_preco = float(input('Insira o novo preço: '))

atualizar_preco(id_produto, novo_preco)
print(produtos)

    


# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

