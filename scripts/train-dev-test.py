import typer
from sklearn.model_selection import train_test_split
import pandas as pd

def main(raw_data: str, train_percent: int):
    df = pd.read_json(raw_data, orient='records', lines=True)
    train, _remains = train_test_split(df, test_size=(100 - train_percent)/100, random_state=0)
    dev, valid = train_test_split(_remains, test_size=de/100, random_state=0)
    df.to_json()