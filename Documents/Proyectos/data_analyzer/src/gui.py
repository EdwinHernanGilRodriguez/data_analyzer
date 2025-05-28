# data_analyzer - By Edwin Gil
# Este script crea una interfaz grafica simple para cargar archivos CSV

# Importacion de librerias necesarias
import tkinter as tk
from tkinter import filedialog, messagebox
from analyzer import analizar_csv  # Importa la funcion de analisis de datos  
from tkinter.scrolledtext import ScrolledText # Mostrar resultados en un widget de texto con scroll

# Clase principal de la aplicacion
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
        self.boton_cargar = tk.Button(ventana, text="Cargar CSV", command=self.cargar_csv)
        self.boton_cargar.pack()
        
        # Cuadro de texto para mostrar resultados
        self.cuadro_texto = ScrolledText(ventana, width=50, height=10)
        self.cuadro_texto.pack(pady=10)
        
    def cargar_csv(self):
        # Abre un cuadro de dialogo para seleccionar un archivo CSV
        ruta_archivo = filedialog.askopenfilename(
            filetypes=[("Archivos CSV", "*.csv")],
            title="Seleccionar archivo CSV"
        )
        if ruta_archivo:
            # Llama a la función de analisis y obtiene el resumen estadistico
            resumen = analizar_csv(ruta_archivo)
            if resumen is not None:
                self.cuadro_texto.delete(1.0, tk.END)  # Limpia el cuadro de texto
                self.cuadro_texto.insert(tk.END, str(resumen)) # Inserta el resumen en el cuadro de texto
                self.cuadro_texto = ScrolledText(ventana, width=90, height=25, font=("Courier", 10))  # Reinicializa el cuadro de texto para que tenga scroll
                # Muestra mensaje de exito
                messagebox.showinfo("Éxito", "Archivo analizado. Revisa la consola para ver el resumen estadístico.")
            else:
                # Si hubo un error en el analisis, muestra advertencia
                messagebox.showwarning("Error", "No se pudo analizar el archivo.")
        else:
            # Si no se selecciono archivo, muestra advertencia
            messagebox.showwarning("Cancelado", "No se seleccionó ningún archivo.")
            
if __name__ == "__main__":
    # Punto de entrada de la aplicación
    ventana = tk.Tk()
    app = DataAnalyzerApp(ventana)
    ventana.mainloop()