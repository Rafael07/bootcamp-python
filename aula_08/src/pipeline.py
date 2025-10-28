import os

from etl import pipeline_etl

files_path: str = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "files")
)
data_format: str = input("Insira o formato do arquivo que deseja (csv ou parquet): ")
lista = []
lista.append(data_format)

pipeline_etl(files_path, lista)
