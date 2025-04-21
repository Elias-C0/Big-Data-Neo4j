import pandas as pd
from dotenv import load_dotenv
import os
from datetime import datetime
import numpy as np

# Inicio del script y timestamp
print(f"Iniciando limpieza: {datetime.now()}")

# Cargar las variables desde config.env
load_dotenv("Scripts/config.env")

# Obtener las rutas desde las variables de entorno
input_file = os.getenv("INPUT_FILE")  # Ruta del archivo de entrada
output_file = os.getenv("OUTPUT_FILE")  # Ruta del archivo de salida

print(f"Tamaño del archivo: {os.path.getsize(input_file) / (1024*1024):.2f} MB")

# Leer el CSV con pandas
print("Leyendo archivo CSV...")
df_playlist = pd.read_csv(
    input_file,
    on_bad_lines="skip"  # Ignora líneas problemáticas
)

# Mostrar información básica
filas_originales = len(df_playlist)
print(f"Filas leídas: {filas_originales}")

# Limpiar nombres de columnas
df_playlist.columns = [col.replace('"', '').replace('name', '').replace(' ', '') for col in df_playlist.columns]

# Eliminar valores problemáticos
print("\nEliminando filas con valores problemáticos...")

# Guardar recuento original para estadísticas
filas_antes = len(df_playlist)

# 1. Eliminar filas con valores nulos en cualquier columna
df_playlist = df_playlist.dropna()
filas_después_null = len(df_playlist)
print(f"Filas eliminadas por valores nulos: {filas_antes - filas_después_null}")

# 2. Definir valores problemáticos
valores_a_eliminar = ['"', "'", '', ' ', '""', "''"]

# Función para verificar si un valor es problemático (optimizada)
def es_valor_problemático(valor):
    if pd.isna(valor):
        return True
    if isinstance(valor, str):
        valor_limpio = valor.strip()
        return valor_limpio in valores_a_eliminar or len(valor_limpio) <= 1
    return False

# Eliminar filas con valores problemáticos en columnas importantes usando listas por comprensión
for columna in df_playlist.columns:
    filas_antes_filtro = len(df_playlist)
    # Crear una lista de índices válidos usando comprensión de listas
    indices_validos = [i for i, valor in enumerate(df_playlist[columna]) if not es_valor_problemático(valor)]
    # Filtrar el DataFrame usando los índices válidos
    df_playlist = df_playlist.iloc[indices_validos]
    print(f"Filas eliminadas por valores problemáticos en '{columna}': {filas_antes_filtro - len(df_playlist)}")

# Información después de limpieza
print(f"\nFilas después de limpieza: {len(df_playlist)}")
print(f"Total filas eliminadas: {filas_originales - len(df_playlist)} ({(filas_originales - len(df_playlist))/filas_originales*100:.2f}%)")

# 3. Limpiar valores dentro de las celdas (usando listas por comprensión)
print("\nLimpiando valores dentro de las celdas...")
for columna in df_playlist.columns:
    if df_playlist[columna].dtype == 'object':  # Solo procesar columnas de texto
        df_playlist[columna] = [valor.replace('"', '').strip() if isinstance(valor, str) else valor for valor in df_playlist[columna]]

# Guardar el archivo limpio
print("\nGuardando archivo limpio...")
df_playlist.to_csv(
    output_file,
    index=False,  # Evita guardar el índice como una columna en el CSV
    sep=",",      # Especifica el delimitador, en este caso una coma
    encoding="utf-8",  # Asegura un correcto manejo de caracteres especiales
    na_rep=""     # Representación para valores NA/NaN
)

# Estadísticas finales
print("\n===== RESUMEN DE LIMPIEZA =====")
print(f"Tiempo final: {datetime.now()}")
print(f"Filas originales: {filas_originales}")
print(f"Filas después de limpieza: {len(df_playlist)}")
print(f"Filas eliminadas: {filas_originales - len(df_playlist)} ({(filas_originales - len(df_playlist))/filas_originales*100:.2f}%)")
print(f"Tamaño original: {os.path.getsize(input_file) / (1024*1024):.2f} MB")
print(f"Tamaño limpio: {os.path.getsize(output_file) / (1024*1024):.2f} MB")
print("Limpieza completada con éxito.")

# Mostrar una pequeña muestra del resultado
print("\nMuestra del dataset limpio (primeras 5 filas):")
print(df_playlist.head())