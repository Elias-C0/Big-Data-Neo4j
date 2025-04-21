import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import csv
from collections import defaultdict, Counter
from dotenv import load_dotenv

def analyze_spotify_dataset(file_path, sample_size=1000, print_samples=5):
    """
    Realiza un análisis exploratorio del conjunto de datos de Spotify
    """
    print(f"Analizando archivo: {file_path}")
    print(f"Tamaño del archivo: {os.path.getsize(file_path) / (1024*1024):.2f} MB")

    # Leer el archivo CSV con pandas
    try:
        df = pd.read_csv(file_path,on_bad_lines='skip', nrows=sample_size)
        print("\n=== MUESTRA DE DATOS ===")
        print(df.head(print_samples))  # Muestra las primeras filas del DataFrame
        print("\n=== INFORMACIÓN DEL DATAFRAME ===")
        print(df.info())  # Muestra información general del DataFrame

         # Mostrar un ejemplo de cada columna
        print("\n=== EJEMPLOS DE VALORES EN CADA COLUMNA ===")
        for col in df.columns:
            example_value = df[col].dropna().iloc[0] if not df[col].dropna().empty else "Valor nulo"
            print(f"{col}: {example_value}")

        # Mostrar estadísticas descriptivas
        print("\n=== ESTADÍSTICAS DESCRIPTIVAS ===")
        print(df.describe(include='all'))  # Incluye todas las columnas, tanto numéricas como categóricas

    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")

# Ejecutar el análisis
load_dotenv("Scripts/config.env")
# Obtener las rutas desde las variables de entorno
file_path = os.getenv("INPUT_FILE")

analyze_spotify_dataset(file_path, sample_size=5000)