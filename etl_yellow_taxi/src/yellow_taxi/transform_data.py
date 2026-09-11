import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:   
    colunas_to_datetime = [
        'tpep_pickup_datetime', 
        'tpep_dropoff_datetime'
    ]
    
    for col in colunas_to_datetime:
        df[col] = pd.to_datetime(
                    df[col],
                    format='%Y-%m-%d %H:%M:%S',
                    errors='coerce'
                )
    return df

def busca_registros_nulos(df:pd.DataFrame) -> int:
    return df.isna().sum()[lambda x: x > 0]
    
def total_registros(df:pd.DataFrame) -> int:
    total_linhas = len(df)
    total_colunas = len(df.columns)
    return total_linhas, total_colunas

def validar_distancia(df:pd.DataFrame) -> pd.DataFrame:
    return (df['trip_distance'] <= 0) | (df['trip_distance'] > 100)

def validar_passageiros(df:pd.DataFrame) -> pd.DataFrame:
    return (
        (df['passenger_count'] <= 0) |
        (df['passenger_count'] > 6)
    )

def tarifa_negativa(df:pd.DataFrame) -> pd.DataFrame:
    return (
        (df['fare_amount'].isna()) |
        (df['fare_amount'] < 0)
    )

def validar_distancia_viagem(df:pd.DataFrame) -> pd.DataFrame:
    return (
        (df['trip_distance'].isna()) |
        (df['trip_distance'] < 0)
    )

def validar_tempo_viagem(df:pd.DataFrame) -> pd.DataFrame:
        
    invalid_duration = (df['tpep_pickup_datetime'] > df['tpep_dropoff_datetime'])
    
    return df[invalid_duration]

def validar_pick_null(df:pd.DataFrame) -> pd.DataFrame:
    invalidos = (
        (df['pickup_longitude'] == 0)       |
        (df['pickup_latitude'] == 0)        
    )

    return df[invalidos]

def validar_pickup_location(df:pd.DataFrame) -> pd.DataFrame:
    invalidos = (
    (df['pickup_latitude'] < 40.4) | 
    (df['pickup_latitude'] > 41.0) |
    (df['pickup_longitude'] < -74.3) | 
    (df['pickup_longitude'] > -73.7)
)

    return df[invalidos]

def validar_dropoff_location(df:pd.DataFrame) -> pd.DataFrame:
    invalidos = (
    (df['dropoff_latitude'] < 40.4) | 
    (df['dropoff_latitude'] > 41.0) |
    (df['dropoff_longitude'] < -74.3) | 
    (df['dropoff_longitude'] > -73.7)
)

    return df[invalidos]