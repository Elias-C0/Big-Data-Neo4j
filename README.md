# Big-Data-Neo4j-Spotify

## Pasos para configurar la conexión a la base de datos

1. Primero, crear un archivo llamado `config.env` en la carpeta `Scripts` y pegar lo siguiente:

```
# Archivo de entrada (ruta completa o relativa)
INPUT_FILE=./Scripts/spotify_dataset.csv

# Archivo de salida (ruta completa o relativa)
OUTPUT_FILE=./Scripts/spotify_clean.csv
```

El archivo ya está en `.gitignore` por lo que va a ser ignorado.

2. Instalá `pip install python-dotenv` y `pip install kagglehub`.

3. Ejecutá `Descarga_archivo.py` y `Limpieza.py`.

## Pasos para configurar Neo4j (Opcional)

1. En caso de querer visualizar más de 300 nodos en Neo4j Browser, hay que cambiar el parametro de visualizacion de cypher:
```
Graph Visualization
Initial Node Display 1000
```

2. Para poder cargar todos los nodos hay que cambiar los parámetros para asignar más memoria a Neo4j (hay que tener cuidado si no tenes mucha ram):

```
dbms.memory.heap.initial_size=2G

dbms.memory.heap.max_size=3G

dbms.memory.transaction.total.max=3G
```
