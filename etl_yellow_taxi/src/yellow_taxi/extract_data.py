import pandas as pd
from pathlib import Path

path_yellow_trip = Path(__file__).parent.parent / 'data' / 'yellow_tripdata_2016-03.csv'

def extract_yellow_tripdata(path:str) -> pd.DataFrame:
    df = pd.read_csv(path)    
    return df