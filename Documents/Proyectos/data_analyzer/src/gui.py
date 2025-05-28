# data_analyzer - By Edwin Gil
# Este script crea una interfaz grafica simple para cargar archivos CSV

# Importacion de librerias necesarias
import tkinter as tk
from tkinter import filedialog, messagebox  

class DataAnalyzerApp:
    def __init__(self, ventana):
        # Iniciar la ventana principal de la aplicacion
        self.ventana = ventana
        self.ventana.title("Data Analyzer - By Edwin Gil") # Titulo de la ventana
        self.ventana.geometry("400x300") # Tamaño de la ventana
        
        # Etiqueta de instrucciones
        self.etiqueta = tk.Label(ventana, text="Carga un archivo CSV para analizar:")
        self.etiqueta.pack(pady=20)
        
        # Boton para cargar el archivo CSV
        self.boton_cargar = tk.Button(ventana, text="Cargar CSV", command=self.load_csv)
        self.boton_cargar.pack()
        
    def cargar_csv(self):
        # Abre un cuadro de dialogo para seleccionar un archivo CSV
        ruta_archivo = filedialog.askopenfilename(
            filetypes=[("Archivos CSV", "*.csv")],
            title="Seleccionar archivo CSV"
        )
        if ruta_archivo:
            # Si se selecciona un archivo, muestra mensaje de éxito
            messagebox.showinfo("Archivo Cargado", f"Archivo cargado: {ruta_archivo}")
        else:
            # Si no se selecciona archivo, muestra advertencia
            messagebox.showwarning("Cancelado", "No se ha seleccionado ningún archivo.")

if __name__ == "__main__":
    # Punto de entrada de la aplicación
    ventana = tk.Tk()
    app = DataAnalyzerApp(ventana)
    ventana.mainloop()