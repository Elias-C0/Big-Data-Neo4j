import csv
import os
from datetime import datetime

def clean_spotify_dataset(input_file, output_file):
    """
    Limpia el dataset de Spotify eliminando filas con número incorrecto de columnas
    y asegurando que no haya problemas de formato.
    """
    start_time = datetime.now()
    print(f"Iniciando limpieza: {start_time}")

    # Estadísticas
    total_rows = 0
    processed_rows = 0
    skipped_rows = 0
    column_distribution = {}

    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, \
             open(output_file, 'w', encoding='utf-8', newline='') as outfile:

            # Leer primera línea para obtener encabezados
            header_line = next(infile)
            expected_columns = header_line.count(',') + 1
            print(f"Encabezados detectados: {expected_columns} columnas")

            # Configurar writer
            writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)

            # Escribir encabezados
            writer.writerow(["user_id", "artistname", "trackname", "playlistname"])

            # Procesar línea por línea para mayor control
            line_num = 1  # Empezamos en 1 porque ya leímos la primera línea
            for line in infile:
                line_num += 1
                total_rows += 1

                # Contar columnas (método básico)
                num_columns = line.count(',') + 1

                # Actualizar estadísticas de distribución de columnas
                if num_columns in column_distribution:
                    column_distribution[num_columns] += 1
                else:
                    column_distribution[num_columns] = 1

                # Saltarse líneas con número incorrecto de columnas
                if num_columns != expected_columns:
                    skipped_rows += 1
                    if skipped_rows <= 5:  # Mostrar solo las primeras 5 líneas saltadas
                        print(f"Saltando línea {line_num}: {num_columns} columnas encontradas")
                    continue

                # Procesar la línea manualmente para asegurar formato correcto
                try:
                    # Intentar analizar la línea con CSV reader
                    fields = list(csv.reader([line]))[0]

                    # Verificar número de campos después del parseo
                    if len(fields) != expected_columns:
                        skipped_rows += 1
                        continue

                    # Limpiar cada campo
                    clean_fields = []
                    for field in fields:
                        # Eliminar comillas adicionales, saltos de línea y espacios extras
                        clean_field = field.strip().replace('\n', ' ').replace('\r', ' ')
                        clean_fields.append(clean_field)

                    # Escribir fila limpia
                    writer.writerow(clean_fields)
                    processed_rows += 1

                    # Mostrar progreso
                    if processed_rows % 100000 == 0:
                        elapsed = datetime.now() - start_time
                        print(f"Procesadas {processed_rows} filas ({skipped_rows} descartadas). Tiempo: {elapsed}")

                except Exception as e:
                    skipped_rows += 1
                    if skipped_rows <= 5:
                        print(f"Error procesando línea {line_num}: {str(e)}")

    except Exception as e:
        print(f"Error general: {str(e)}")

    # Resumen final
    end_time = datetime.now()
    elapsed = end_time - start_time

    print("\n===== RESUMEN DE LIMPIEZA =====")
    print(f"Tiempo total: {elapsed}")
    print(f"Filas totales procesadas: {total_rows}")
    print(f"Filas conservadas: {processed_rows} ({processed_rows/total_rows*100:.2f}%)")
    print(f"Filas descartadas: {skipped_rows} ({skipped_rows/total_rows*100:.2f}%)")

    print("\nDistribución de columnas:")
    for cols, count in sorted(column_distribution.items()):
        print(f"  {cols} columnas: {count} filas ({count/total_rows*100:.2f}%)")

    print(f"\nArchivo limpio guardado en: {output_file}")
    print(f"Tamaño original: {os.path.getsize(input_file) / (1024*1024):.2f} MB")
    print(f"Tamaño limpio: {os.path.getsize(output_file) / (1024*1024):.2f} MB")

# Ejecutar limpieza
input_file = "spotify_dataset.csv"  # Ajusta la ruta según corresponda
output_file = "spotify_clean.csv"
clean_spotify_dataset(input_file, output_file)