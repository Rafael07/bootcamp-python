import os
from pprint import pprint

from etl import formated_output, group_by_category, read_csv, total_sales_by_product

path_csv_file = os.path.join(os.path.dirname(__file__), "..", "files", "vendas.csv")

minha_lista = read_csv(path_csv_file)
meu_filtro = group_by_category(minha_lista)
vendas = total_sales_by_product(meu_filtro)

pprint(formated_output(vendas))
