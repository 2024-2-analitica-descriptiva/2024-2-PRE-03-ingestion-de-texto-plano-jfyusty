"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    import pandas as pd  # Importa la librería pandas para trabajar con estructuras de datos como DataFrames.
    import re  # Importa el módulo re para trabajar con expresiones regulares.

    # Lee el archivo de texto y lo convierte en una lista de líneas.
    file_path = 'files/input/clusters_report.txt'  # Define la ruta del archivo a procesar.
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()  # Lee todas las líneas del archivo en una lista.
    
    # Extrae las líneas relevantes (omitiendo encabezados y líneas separadoras).
    data_lines = lines[4:]  # Omite las primeras 4 líneas (encabezado y separador).

    # Inicializa una lista vacía para almacenar las filas procesadas.
    rows = []
    current_row = []  # Variable temporal para almacenar las líneas de un único cluster.

    # Procesa cada línea para agrupar datos relacionados con el mismo cluster.
    for line in data_lines:
        if re.match(r'^\s*\d+\s+', line):  # Verifica si la línea inicia con un número (nuevo cluster).
            if current_row:  # Si hay datos en `current_row`, agrégalos a la lista de filas.
                rows.append(current_row)
            current_row = [line.strip()]  # Inicia una nueva fila para el nuevo cluster.
        else:
            current_row.append(line.strip())  # Añade líneas adicionales al cluster actual.

    # Agrega la última fila al final del procesamiento.
    if current_row:
        rows.append(current_row)

    # Inicializa una lista para almacenar las filas procesadas.
    processed_rows = []

    # Procesa cada fila para extraer y estructurar los datos.
    for row in rows:
        row_data = " ".join(row)  # Combina todas las líneas de un cluster en una sola cadena.
        parts = re.split(r'\s{2,}', row_data)  # Divide la cadena en partes usando dos o más espacios como delimitador.
        cluster_number = int(parts[0])  # Extrae el número del cluster como entero.
        keyword_count = int(parts[1])  # Extrae la cantidad de palabras clave como entero.
        keyword_percentage = parts[2].replace(',', '.').strip('%')  # Extrae y limpia el porcentaje de palabras clave.
        keywords = " ".join(parts[3:])  # Combina las palabras clave en una sola cadena.
        keywords = re.sub(r'\s+', ' ', keywords)  # Normaliza los espacios múltiples en las palabras clave.
        keywords = keywords.strip()  # Elimina espacios al principio y al final.
        keywords = keywords.replace(' ,', ',')  # Corrige espacios antes de comas.
        keywords = keywords.replace(', ', ', ').replace(', ', ', ').strip(', ')  # Asegura separación correcta entre palabras clave.
        keywords = keywords.rstrip('.')  # Eliminar el punto final
        processed_rows.append({  # Añade los datos estructurados como un diccionario.
            'cluster': cluster_number,
            'cantidad_de_palabras_clave': keyword_count,
            'porcentaje_de_palabras_clave': float(keyword_percentage),  # Convierte el porcentaje a un número flotante.
            'principales_palabras_clave': keywords  # Inserta las palabras clave formateadas correctamente.
        })

    # Crea un DataFrame a partir de los datos procesados.
    df = pd.DataFrame(processed_rows)

    # Convierte los nombres de las columnas a minúsculas y reemplaza los espacios con guiones bajos.
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    return df

# Llamar a la función y obtener los resultados
df_arreglado = pregunta_01()
print(df_arreglado)