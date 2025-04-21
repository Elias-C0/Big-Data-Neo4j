import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import csv
from collections import defaultdict, Counter

def analyze_spotify_dataset(file_path, sample_size=1000, print_samples=5):
    """
    Realiza un análisis exploratorio del conjunto de datos de Spotify
    """
    print(f"Analizando archivo: {file_path}")
    print(f"Tamaño del archivo: {os.path.getsize(file_path) / (1024*1024):.2f} MB")

    # Primero intenta leer las primeras líneas para entender la estructura
    print("\n=== MUESTRA DE PRIMERAS LÍNEAS ===")
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for i, line in enumerate(f):
            if i >= print_samples:
                break
            print(f"Línea {i+1}: {line.strip()}")

    # Análisis de estructura del CSV
    print("\n=== ANÁLISIS DE ESTRUCTURA DE LÍNEAS ===")
    column_counts = Counter()
    problem_lines = []

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        # Leer encabezados
        header_line = next(f, None)
        if header_line:
            header_columns = header_line.count(',') + 1
            print(f"Encabezados detectados: {header_columns} columnas")
            print(f"Contenido de encabezados: {header_line.strip()}")

        # Analizar estructura de las primeras filas
        for i, line in enumerate(f):
            if i >= sample_size:
                break

            # Contar columnas (manera básica - puede fallar si hay comas dentro de comillas)
            num_columns = line.count(',') + 1
            column_counts[num_columns] += 1

            # Guardar líneas problemáticas (diferentes al número esperado de columnas)
            if num_columns != header_columns:
                if len(problem_lines) < 5:  # Guardar solo algunas para no sobrecargar la memoria
                    problem_lines.append((i+2, line.strip()))  # i+2 porque i es 0-based y ya pasamos el encabezado

    print(f"\nDistribución de número de columnas en las primeras {sample_size} filas:")
    for num_cols, count in sorted(column_counts.items()):
        print(f"  {num_cols} columnas: {count} filas ({count/sample_size*100:.1f}%)")

    if problem_lines:
        print("\n=== EJEMPLOS DE LÍNEAS PROBLEMÁTICAS ===")
        for line_num, content in problem_lines:
            print(f"Línea {line_num}: {content[:150]}..." if len(content) > 150 else f"Línea {line_num}: {content}")

    # Intentar cargar una muestra con pandas para análisis más detallado
    print("\n=== ANÁLISIS DETALLADO DE MUESTRA ===")
    try:
        # Intentar diferentes configuraciones de parser
        parsing_methods = [
            {"name": "Método básico", "params": {"nrows": sample_size}},
            {"name": "Método con quoting", "params": {"nrows": sample_size, "quoting": csv.QUOTE_ALL}},
            {"name": "Método con engine python", "params": {"nrows": sample_size, "engine": "python"}},
            {"name": "Método con error_bad_lines=False", "params": {"nrows": sample_size, "on_bad_lines": "skip"}}
        ]

        for method in parsing_methods:
            try:
                print(f"\nIntentando: {method['name']}")
                sample_df = pd.read_csv(file_path, **method['params'])
                print(f"Lectura exitosa. Dimensiones: {sample_df.shape}")

                print("\nEjemplo de datos:")
                print(sample_df.head())

                print("\nEstadísticas descriptivas:")
                print(sample_df.describe(include='all'))

                print("\nTipos de datos:")
                print(sample_df.dtypes)

                print("\nVerificando valores nulos:")
                null_counts = sample_df.isnull().sum()
                print(null_counts)

                # Si hay valores no nulos en cada columna, mostrar ejemplos
                print("\nEjemplos de valores en cada columna:")
                for col in sample_df.columns:
                    non_null_values = sample_df[col].dropna().unique()[:5]
                    print(f"{col}: {non_null_values}")

                # Análisis de longitud de valores
                print("\nEstadísticas de longitud de texto:")
                for col in sample_df.columns:
                    if sample_df[col].dtype == 'object':
                        sample_df[f'{col}_length'] = sample_df[col].astype(str).str.len()
                        length_stats = sample_df[f'{col}_length'].describe()
                        print(f"{col}: min={length_stats['min']}, max={length_stats['max']}, mean={length_stats['mean']:.1f}")

                # Romper el bucle si una de las configuraciones funciona
                break
            except Exception as e:
                print(f"Error con este método: {str(e)}")

    except Exception as e:
        print(f"No se pudo analizar con pandas: {str(e)}")

# Ejecutar el análisis
file_path = "spotify_dataset.csv"  # Cambia esto a la ruta correcta de tu archivo
analyze_spotify_dataset(file_path, sample_size=5000)