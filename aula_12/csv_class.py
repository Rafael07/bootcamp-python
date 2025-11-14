import pandas as pd


class CsvProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)

    def filtrar_por(self, coluna, valor):
        return self.df[self.df[coluna] == valor]


arquivo_csv = "./exemplo.csv"
coluna = input("Insira uma coluna para filtrar: ")
valor = input("Insira o valor que deseja filtrar: ")

meu_csv = CsvProcessor(arquivo_csv)
meu_csv.carregar_csv()
print(meu_csv.filtrar_por(coluna, valor))
