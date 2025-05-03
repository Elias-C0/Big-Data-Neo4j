<h1 align="center"> 🎧 Big Data con Neo4j & Spotify</h1>

> [!NOTE]
> **Objetivo del proyecto:** Modelar y explorar datos musicales utilizando **Neo4j** como base de datos orientadas a grafos.
>
> Este pipeline empieza con la descarga de datos desde **Kaggle**, seguida por un proceso de limpieza. Después, cargamos los datos en Neo4j y se establecen relaciones con consultas **Cypher**, para posteriormente, analizar las conexiones entre artistas, géneros y canciones.
>

<h2 align="center">🛠 Tecnologías Utilizadas</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Limpieza-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Kaggle-Datasets-20BEFF?logo=kaggle&logoColor=white" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Neo4j-Base%20de%20Datos-008CC1?logo=neo4j&logoColor=green" />
  <img src="https://img.shields.io/badge/Cypher-Consultas-00A86B?logo=codeforces&logoColor=white" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Spotify-Datos%20Musicales-1DB954?logo=spotify&logoColor=green" />
</p>

---

<details>

  <summary>⚙️ Pasos para configurar la conexión a la base de datos</summary>

  1. Crear un archivo llamado config.env dentro de la carpeta Scripts y pegar lo siguiente:
  
  
```env
  # Archivo de entrada (ruta completa o relativa)
  INPUT_FILE=./Scripts/spotify_dataset.csv
  
  # Archivo de salida (ruta completa o relativa)
  OUTPUT_FILE=./Scripts/spotify_clean.csv
```

  > ℹ️ **Nota:** Este archivo ya está incluido en .gitignore, por lo tanto no se subirá al repositorio.

  2. Instalar las librerías necesarias:
  
  
```bash
  pip install python-dotenv
  pip install kagglehub
```
  
  3. Ejecutar los scripts en orden:
  
```bash
  python Descarga_archivo.py
  python Limpieza.py
```
</details>

---

<details> <summary> 🧠 Configuración de Neo4j (opcional) </summary>
  
Si querés visualizar más de 300 nodos es importante que se configure en el Browser de Neo4j:

1. Aumentá el límite de nodos visibles en el Browser de Neo4j:

```Browser Settings
Graph Visualization
Initial Node Display: 1000
```

2. Asigná más memoria a Neo4j para cargar grandes volúmenes de datos (con precaución si tenés poca RAM):

```Settings
dbms.memory.heap.initial_size=2G
dbms.memory.heap.max_size=3G
dbms.memory.transaction.total.max=3G
```

> ⚠️ **Importante:**
>Estos valores son recomendados para equipos con al menos 8GB de RAM. Si tenés menos, ajustalos con cuidado.

</details>

---
<div align="center">
<h2 align="center">👨‍💻 Autores</h2>
<p align="center">
  <table>
    <tr>
      <td align="center">
        <a href="https://www.linkedin.com/in/c-elias-3a8065307/" target="_blank">
          <img src="https://avatars.githubusercontent.com/u/141202551" width="80" height="80" /><br>
          <img src="https://img.shields.io/badge/LinkedIn-Coradini%20Elias-0A66C2?style=sociale&logo=linkedin" />
        </a>
      </td>
      <td align="center">
        <a href="https://www.linkedin.com/in/axelescalante0/" target="_blank">
          <img src="https://avatars.githubusercontent.com/u/141271318" width="80" height="80" /><br>
          <img src="https://img.shields.io/badge/LinkedIn-Escalante%20Axel-0A66C2?style=sociale&logo=linkedin" />
        </a>
      </td>
      <td align="center">
        <a href="https://www.linkedin.com/in/ayrton-milessi-90ab91327/" target="_blank">
          <img src="https://avatars.githubusercontent.com/u/141248568?s=80" width="80" height="80" /><br>
          <img src="https://img.shields.io/badge/LinkedIn-Milessi%20Ayrton-0A66C2?style=sociale&logo=linkedin" />
        </a>
      </td>
      <td align="center">
        <a href="https://www.linkedin.com/in/adriel-starchevich" target="_blank">
          <img src="https://avatars.githubusercontent.com/u/102241028?s=80" width="80" height="80" /><br>
          <img src="https://img.shields.io/badge/LinkedIn-Starchevich%20Adriel-0A66C2?style=sociale&logo=linkedin" />
        </a>
      </td>
    </tr>
  </table>
</p>
</div>


---


>[!NOTE]
>
>En esta imagen están representados solo 10.000 filas
<details>
  <summary> 🌌 Visualización del grafo  </summary>
<p align="center">
  <img src="https://raw.githubusercontent.com/Elias-C0/Big-Data-Neo4j/main/graph.svg" width="800px" alt="Graph" />
</p>
</details>
