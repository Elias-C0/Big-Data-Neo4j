import pandas as pd
from dotenv import load_dotenv
import os

# Cargar las variables desde config.env
load_dotenv("Scripts/config.env")

# Obtener las rutas desde las variables de entorno
input_file = os.getenv("INPUT_FILE")  # Ruta del archivo de entrada
output_file = os.getenv("OUTPUT_FILE")  # Ruta del archivo de salida


df_playlist = pd.read_csv(
    input_file,
    on_bad_lines="skip"  # Ignora líneas problemáticas
)

df_playlist.columns = df_playlist.columns.str.replace('"', '')
df_playlist.columns = df_playlist.columns.str.replace('name', '')
df_playlist.columns = df_playlist.columns.str.replace(' ', '')
df_playlist.columns

df_playlist['track'] = df_playlist['track'].str.replace(r'\s*[\'"“”]+\s*', ' ', regex=True)

df_playlist.to_csv(
    output_file,
    index=False,  # Evita guardar el índice como una columna en el CSV
    sep=",",  # Especifica el delimitador, en este caso una coma
    encoding="utf-8"  # Asegura un correcto manejo de caracteres especiales
)

print("Archivo creado!!")