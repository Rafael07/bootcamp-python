import csv

path: str = 'exemplo.csv'

lista: list = []

with open(path, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for rows in leitor_csv:
        lista.append(rows)

print(lista)