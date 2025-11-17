# preprocesamiento.py
# Funciones básicas de preprocesamiento para Ciencia de Datos

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def cargar_datos(ruta_csv):
    """Carga un dataset CSV en un DataFrame de pandas."""
    return pd.read_csv(ruta_csv)

def eliminar_duplicados(df):
    """Elimina filas duplicadas."""
    return df.drop_duplicates()

def rellenar_nulos(df):
    """Rellena valores nulos con la media o la moda según el tipo de dato."""
    for columna in df.columns:
        if df[columna].dtype in ['int64', 'float64']:
            df[columna].fillna(df[columna].mean(), inplace=True)
        else:
            df[columna].fillna(df[columna].mode()[0], inplace=True)
    return df

def escalar_datos(df):
    """Escala valores numéricos entre 0 y 1."""
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    scaler = MinMaxScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])
    return df

def preprocesar_dataset(ruta_csv):
    """Pipeline completo de preprocesamiento."""
    df = cargar_datos(ruta_csv)
    df = eliminar_duplicados(df)
    df = rellenar_nulos(df)
    df = escalar_datos(df)
    return df

if __name__ == "__main__":
    print("Módulo de preprocesamiento listo.")
