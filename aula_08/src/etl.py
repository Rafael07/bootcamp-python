import glob
import os

import pandas as pd

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
path_json = glob.glob(os.path.join(root_path, "*.json"))


def extract_data(directory: str) -> pd.DataFrame:

    df_list = pd.concat([pd.read_json(files) for files in path_json], ignore_index=True)
    return df_list
