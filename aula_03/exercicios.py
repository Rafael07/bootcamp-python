### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

# def number_checker(quantidade, preco):
#     if quantidade > 0 and preco > 0:
#         return "Os valores são positivos, portanto, válidos!"
#     else:
#         return "Quantidade e preço devem ser sempre positivos, reveja os valores de entrada!"

# qtd = int(input("Insira a quantidade de itens para esse produto: "))
# preco = float(input("Insira o valor do produto: "))

# print(number_checker(qtd, preco))
        


### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que: Temperatura < 18°C é 'Baixa', 
# Temperatura >= 18°C e <= 26°C é 'Normal', Temperatura > 26°C é 'Alta'

# def sensor_analyze(temperature):
#     if temperature < 18:
#         return "Baixa"
#     elif temperature >= 18 and temperature <= 26:
#         return "Normal"
#     elif temperature > 26:
#         return "Alta"

# temp = int(input("Informe a temperatura do sensor: "))
# print(sensor_analyze(temp))

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# def log_analyzer(msg):
#     import datetime

#     if msg == 'ERROR':
#         data = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
#         log = {
#             'timestamp': data,
#             'level': msg,
#             'message': 'Falha na conexão'
#         }
#         return log
#     else:
#         return "Normalidade"

# print(log_analyzer(msg='ERROR'))

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
# import re

# padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# try:
#     idade = int(input("Insira sua idade: "))
#     if not 18 <= idade <= 65:
#         print("Idade fora do intervalo de 18 a 65 anos.")
#     email = input("Insira seu e-mail: ")
#     if not re.match(padrao_email, email):
#         print("E-mail inválido.")
# except:
#     print("Erro")

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# transacao = {'valor': 1000, 'hora': 9}

# if transacao['valor'] > 10000 or not (9 <= transacao['hora'] <= 18):
#     print("Transação suspeita, fazer verificações mais profundas!")
# else:
#     print("Transação normal!")


### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# import string
# def unique_words_counter(frase):
#     lista = frase.split()
#     dicionario = {}
#     for palavra in lista:
#         palavra = palavra.strip(string.punctuation)
#         if palavra in dicionario:
#             dicionario[palavra] += 1
#         else:
#             dicionario[palavra] = 1
#     return dicionario

# frase = input("Insira uma frase: ")
# print(unique_words_counter(frase))

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# valores = [10, 20, 30, 40, 50]

# def normalizar_valores(valores):
#     # normal =[]
#     # for valor in valores:
#     #     novo_valor = ((valor - min(valores)) / (max(valores) - min(valores)))
#     #     normal.append(novo_valor)
#     normal = [((valor - min(valores)) / (max(valores) - min(valores))) for valor in valores] # list comprehesion
#     return normal

# print(normalizar_valores(valores))

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# usuarios = [
#     {"id": 1, "nome": "João", "idade": 25, "email": "joao@example.com"},
#     {"id": 2, "nome": "Maria", "idade": 30},
#     {"id": 3, "nome": "Pedro", "email": "pedro@example.com", "telefone": "123456789"},
#     {"id": 4, "nome": "Ana", "idade": 20, "email": "ana@example.com", "telefone": "987654321"},
#     {"id": 5, "nome": "Carlos"},
#     {"id": 6, "nome": "Luisa", "idade": 35, "email": "luisa@example.com"},
#     {"id": 7, "telefone": "555555555"},
#     {"id": 8, "nome": "Gabriel", "idade": 28, "email": "gabriel@example.com"}
# ]

# sem_nome = [usuario['id'] for usuario in usuarios if 'nome' not in usuario]
# sem_idade = [usuario['id'] for usuario in usuarios if 'idade' not in usuario] 
# sem_email = [usuario['id'] for usuario in usuarios if 'email' not in usuario]
# sem_telefone = [usuario['id'] for usuario in usuarios if 'telefone' not in usuario]

# print(f"ID's sem nome: {sem_nome}")
# print(f"ID's sem idade: {sem_idade}")
# print(f"ID's sem email: {sem_email}")
# print(f"ID's sem telefone: {sem_telefone}")

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# numeros = [num for num in range(1,100)]

# pares = [num for num in numeros if (num % 2) == 0]
# print(f'Numeros pares: {pares}')
# print(f'Quantidade de pares: {len(pares)}')

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {'id': 1, 'categoria': 'Eletrônicos', 'valor': 1200.00},
    {'id': 2, 'categoria': 'Roupas', 'valor': 250.00},
    {'id': 3, 'categoria': 'Alimentos', 'valor': 80.00},
    {'id': 4, 'categoria': 'Eletrônicos', 'valor': 850.00},
    {'id': 5, 'categoria': 'Roupas', 'valor': 400.00},
    {'id': 6, 'categoria': 'Alimentos', 'valor': 150.00},
    {'id': 7, 'categoria': 'Livros', 'valor': 90.00},
    {'id': 8, 'categoria': 'Eletrônicos', 'valor': 2200.00},
    {'id': 9, 'categoria': 'Livros', 'valor': 120.00},
    {'id': 10, 'categoria': 'Roupas', 'valor': 180.00},
]

totais = {}

for registro in vendas:
    categoria = registro['categoria']
    valor = registro['valor']

    if categoria in totais:
        totais[categoria] += valor
    else:
        totais[categoria] = valor

for categoria, total in totais.items():
    print(f'Total de vendas para {categoria.lower()}: R${total:.2f}')



