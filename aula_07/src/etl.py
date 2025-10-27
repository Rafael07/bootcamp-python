import csv
import os
from collections import defaultdict

path_csv_file = os.path.join(os.path.dirname(__file__), "..", "files", "vendas.csv")


def read_csv(csv_file: str) -> list[dict]:
    """
    Função que lê um arquivo csv e retorna uma lista
    de dicionários.
    """

    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        csv_list = list(reader)
    return csv_list


def group_by_category(file_list: list) -> defaultdict[str, list]:
    """
    Funcao que agrega produtos por categoria em um dicionario
    """
    products_by_category: dict = defaultdict(list)
    for row in file_list:
        category = row["Categoria"]
        product_info = {
            "Produto": row["Produto"],
            "Quantidade": row["Quantidade"],
            "Venda": row["Venda"],
        }
        products_by_category[category].append(product_info)
    return products_by_category


def total_sales_by_product(grouped_dict: dict) -> dict[str, dict[str, float]]:
    """
    Funcao que calcula o total vendido por produto
    """
    totals_by_category: dict[str, dict[str, float]] = defaultdict(
        lambda: defaultdict(float)
    )
    for category, rows in grouped_dict.items():
        for row in rows:
            product = row["Produto"]
            quantity = int(row["Quantidade"])
            price = float(row["Venda"])
            totals_by_category[category][product] += quantity * price
    return totals_by_category


def formated_output(
    totals_by_category: dict[str, dict[str, float]]
) -> dict[str, dict[str, float]]:
    return {
        category: {product: round(value, 2) for product, value in products.items()}
        for category, products in totals_by_category.items()
    }


# minha_lista = read_csv(path_csv_file)
# meu_filtro = group_by_category(minha_lista)
# vendas = total_sales_by_product(meu_filtro)

# pprint.pprint(formated_output(vendas))
