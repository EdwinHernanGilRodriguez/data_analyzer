# data_analyzer - By Edwin Gil

# Importacion de librerias necesarias
import pandas as pd # Para el analisis de datos
from tabulate import tabulate # Para mostrar resultados en formato tabular

# Funcion para analizar un archivo CSV y devolver un resumen estadístico
def analizar_csv(ruta_archivo):
    try:
        # Lee el archivo CSV en un DataFrame de pandas
        df = pd.read_csv(ruta_archivo)
        # Genera un resumen estadistico de todas las columnas
        resumen = df.describe(include='all').transpose()
        # Retorna el resumen en formato tabular
        return tabulate(resumen, headers='keys', tablefmt='grid')
    except Exception as e:
        # Manejo de errores: imprime el error y retorna None
        print(f"Error al analizar el archivo CSV: {e}")
        return None