import pandas as pd
import os
from dotenv import load_dotenv

def analyze_spotify_dataset(file_path, print_samples=5):
    """
    Hace un análisis exploratorio del conjunto de datos de Spotify
    """
    print(f"Analizando archivo: {file_path}")
    print(f"Tamaño del archivo: {os.path.getsize(file_path) / (1024*1024):.2f} MB")

    # Lee el archivo CSV con pandas
    try:
        df = pd.read_csv(file_path,on_bad_lines='skip')
        print("\n=== MUESTRA DE DATOS ===")
        print(df.head(print_samples))  # Muestra las primeras filas del DataFrame
        print("\n=== INFORMACIÓN DEL DATAFRAME ===")
        print(df.info())  # Muestra información general del DataFrame

        # Muestra un ejemplo de cada columna
        print("\n=== EJEMPLOS DE VALORES EN CADA COLUMNA ===")
        for col in df.columns:
            example_value = df[col].dropna().iloc[0] if not df[col].dropna().empty else "Valor nulo"
            print(f"{col}: {example_value}")

        # Muestra estadísticas
        print("\n=== ESTADÍSTICAS ===")
        print(df.describe(include='all'))

    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")

# Obtiene las rutas desde las variables de entorno
load_dotenv("Scripts/config.env")
file_path = os.getenv("INPUT_FILE")

analyze_spotify_dataset(file_path)