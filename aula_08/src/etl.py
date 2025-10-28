import glob
import os

import pandas as pd

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
files_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "files"))
path_json = glob.glob(os.path.join(root_path, "*.json"))


def extract_data(directory: str) -> pd.DataFrame:
    """
    Funcao que extrai os dados de arquivos JSON e os consolida em um DataFrame
    """
    df_list = pd.concat([pd.read_json(files) for files in path_json], ignore_index=True)
    return df_list


def kpi_total_sales(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula KPI de total de vendas
    """
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


def load_data(df: pd.DataFrame, input: list):
    """
    Dada entrada de uma opção salva em lista,
    definir se arquivo e salvo em csv ou parquet
    """
    for item in input:
        if item == "csv":
            output_path = os.path.join(files_path, "data.csv")
            df.to_csv(output_path, index=False)
        if item == "parquet":
            output_path = os.path.join(files_path, "data.parquet")
            df.to_parquet(output_path)


def pipeline_etl(source_path: str, output_option: list):
    data_frame = extract_data(source_path)
    kpi_dataframe = kpi_total_sales(data_frame)
    load_data(kpi_dataframe, output_option)
