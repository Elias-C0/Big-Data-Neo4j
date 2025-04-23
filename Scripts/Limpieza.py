import pandas as pd
from dotenv import load_dotenv
import os

# Carga las variables desde config.env
load_dotenv("Scripts/config.env")

# Obtiene las rutas desde las variables de entorno
input_file = os.getenv("INPUT_FILE")  # Archivo de entrada
output_file = os.getenv("OUTPUT_FILE")  # Achivo de salida


df_playlist = pd.read_csv(
    input_file,
    on_bad_lines="skip"  # Ignora líneas
)

# Limpia los nombres de las columnas del DataFrame
df_playlist.columns = df_playlist.columns.str.replace('"', '')  # Elimina comillas doble
df_playlist.columns = df_playlist.columns.str.replace(' ', '')  # Elimina espacios
df_playlist.columns

# Limpia los valores de la columna 'trackname'
df_playlist['trackname'] = df_playlist['trackname'].str.replace(
    r'\s*[\'"“”]+\s*', ' ', regex=True  # Reemplaza comillas simples, dobles y otros caracteres similares por un espacio
)
df_playlist.to_csv(
    output_file,
    index=False,  # Evita guardar el índice como una columna en el CSV
    sep=",",  # Especifica el delimitador
    encoding="utf-8"
)

print("Archivo creado!!")