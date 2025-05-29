# data_analyzer - By Edwin Gil
# Este script crea una interfaz gráfica para cargar archivos CSV y analizarlos

import tkinter as tk  # Librería para crear interfaces gráficas
from tkinter import filedialog, messagebox  # Para diálogos de archivos y mensajes
from analyzer import generar_resumen_estadistico  # Función para análisis desde analyzer.py
from tkinter.scrolledtext import ScrolledText  # Widget de texto con scroll
import pandas as pd  # Librería para manejo de datos

# Clase principal de la aplicación
class DataAnalyzerApp:
    def __init__(self, ventana):
        # Configuración de la ventana principal
        self.ventana = ventana
        self.ventana.title("Data Analyzer - By Edwin Gil")
        self.ventana.geometry("400x300")

        # Etiqueta de instrucciones
        self.etiqueta = tk.Label(ventana, text="Carga un archivo CSV para analizar:")
        self.etiqueta.pack(pady=20)

        # Botón para cargar el archivo CSV
        self.boton_cargar = tk.Button(ventana, text="Cargar CSV", command=self.cargar_csv)
        self.boton_cargar.pack()

        # Cuadro de texto para mostrar resultados y análisis
        self.cuadro_texto = ScrolledText(ventana, width=140, height=50)
        self.cuadro_texto.pack(pady=10)

    # Método para cargar un archivo CSV seleccionado por el usuario
    def cargar_csv(self):
        ruta_archivo = filedialog.askopenfilename(
            filetypes=[("Archivos CSV", "*.csv")],
            title="Seleccionar archivo CSV"
        )
        if ruta_archivo:
            try:
                # Se lee el archivo CSV y se carga en un DataFrame de pandas
                self.df = pd.read_csv(ruta_archivo)
                # Se muestran las opciones de análisis disponibles
                self.mostrar_opciones_analisis()
            except Exception as e:
                # Se muestra un mensaje de error si no se puede leer el archivo
                messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")
        else:
            # Mensaje de advertencia si el usuario cancela la selección de archivo
            messagebox.showwarning("Cancelado", "No se seleccionó ningún archivo.")

    # Método para mostrar las opciones de análisis una vez cargado el CSV
    def mostrar_opciones_analisis(self):
        # Se muestra una vista previa de los datos cargados en el cuadro de texto
        self.cuadro_texto.delete(1.0, tk.END)
        self.cuadro_texto.insert(tk.END, "Vista previa de los datos cargados:\n")
        self.cuadro_texto.insert(tk.END, str(self.df.head()))

        # Ventana emergente para seleccionar el tipo de análisis a realizar
        ventana_opciones = tk.Toplevel(self.ventana)
        ventana_opciones.title("Opciones de Análisis")
        ventana_opciones.geometry("300x150")

        tk.Label(ventana_opciones, text="¿Qué deseas hacer?").pack(pady=10)

        # Botón para analizar todo el archivo
        tk.Button(
            ventana_opciones,
            text="Analizar todo el archivo",
            command=lambda: [self.analizar_todo(), ventana_opciones.destroy()]
        ).pack(pady=5)

        # Botón para seleccionar columnas específicas para el análisis
        tk.Button(
            ventana_opciones,
            text="Seleccionar columnas",
            command=lambda: [self.mostrar_selector_columnas(), ventana_opciones.destroy()]
        ).pack(pady=5)

    # Método para analizar todo el archivo
    def analizar_todo(self):
        resumen = generar_resumen_estadistico(self.df)
        self.cuadro_texto.delete(1.0, tk.END)
        self.cuadro_texto.insert(tk.END, "Análisis Estadístico (todo el archivo):\n")
        self.cuadro_texto.insert(tk.END, resumen)

    # Método para mostrar la ventana de selección de columnas
    def mostrar_selector_columnas(self):
        ventana_columnas = tk.Toplevel(self.ventana)
        ventana_columnas.title("Seleccionar Columnas")
        ventana_columnas.geometry("300x400")

        seleccion = {}

        # Se crean checkbuttons para cada columna del DataFrame
        for columna in self.df.columns:
            var = tk.BooleanVar()
            tk.Checkbutton(ventana_columnas, text=columna, variable=var).pack(anchor='w')
            seleccion[columna] = var

        # Método para confirmar las columnas seleccionadas
        def confirmar_columnas():
            columnas_seleccionadas = [col for col, var in seleccion.items() if var.get()]
            if columnas_seleccionadas:
                df_filtrado = self.df[columnas_seleccionadas]
                resumen = generar_resumen_estadistico(df_filtrado)
                self.cuadro_texto.delete(1.0, tk.END)
                self.cuadro_texto.insert(tk.END, f"Análisis Estadístico (columnas seleccionadas):\n")
                self.cuadro_texto.insert(tk.END, resumen)
            else:
                messagebox.showwarning("Sin selección", "Debes seleccionar al menos una columna.")
            ventana_columnas.destroy()

        # Botón para analizar la selección de columnas
        tk.Button(ventana_columnas, text="Analizar selección", command=confirmar_columnas).pack(pady=10)

# Inicio de la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()
    app = DataAnalyzerApp(ventana)
    ventana.mainloop()