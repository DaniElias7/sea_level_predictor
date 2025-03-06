import pandas as pd

def load_data(file_path: str = 'data/epa-sea-level.csv') -> pd.DataFrame:
    df = pd.read_csv(file_path)

    return df
