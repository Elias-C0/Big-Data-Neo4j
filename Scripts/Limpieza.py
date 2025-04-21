import pandas as pd

df_playlist = pd.read_csv(
    "C:/Users/Elias/.Neo4jDesktop/relate-data/dbmss/dbms-d80e22ad-ccfd-4af9-b25b-7a0d123cddec/import/spotify_dataset.csv",
    on_bad_lines="skip"  # Ignora líneas problemáticas
)

df_playlist.columns = df_playlist.columns.str.replace('"', '')
df_playlist.columns = df_playlist.columns.str.replace('name', '')
df_playlist.columns = df_playlist.columns.str.replace(' ', '')
df_playlist.columns

df_playlist.to_csv(
    "C:/Users/Elias/.Neo4jDesktop/relate-data/dbmss/dbms-d80e22ad-ccfd-4af9-b25b-7a0d123cddec/import/spotify_clean.csv",  # Ruta donde guardarás el archivo
    index=False,  # Evita guardar el índice como una columna en el CSV
    sep=",",  # Especifica el delimitador, en este caso una coma
    encoding="utf-8"  # Asegura un correcto manejo de caracteres especiales
)