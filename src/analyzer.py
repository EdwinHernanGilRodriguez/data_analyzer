# data_analyzer - By Edwin Gil

# Importación de librerías necesarias
import pandas as pd  # Para el análisis de datos
from tabulate import tabulate  # Para mostrar resultados en formato tabular

# Función para generar un resumen estadístico de un DataFrame
def generar_resumen_estadistico(df):
    try:
        # Calcula estadísticas descriptivas (numéricas y categóricas)
        resumen = df.describe(include='all').transpose()
        # Retorna el resumen en formato tabular legible
        return tabulate(resumen, headers='keys', tablefmt='grid')
    except Exception as e:
        # Manejo de errores
        return f"Error al generar análisis estadístico: {e}"

# Función adicional si se requiere análisis desde un archivo
def analizar_csv(ruta_archivo):
    try:
        df = pd.read_csv(ruta_archivo)
        return generar_resumen_estadistico(df)
    except Exception as e:
        print(f"Error al analizar el archivo CSV: {e}")
        return None