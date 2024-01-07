import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import main
import subprocess


#Variables globales
nombre_archivo = ""

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        nombre_archivo = archivo
        # archivo = archivo.split("/")[-1]
        entry_archivo.config(state="normal")
        entry_archivo.delete(0, tk.END)
        entry_archivo.insert(0, archivo)
        entry_archivo.config(state="readonly")

        caja_texto.config(state="normal")
        caja_texto.delete("1.0", tk.END)
        caja_texto.config(state="disabled")


        boton_analizar.config(state="normal")
        boton_ver_codigo.config(state="normal")
        boton_ver_arbol.config(state="disabled")
        boton_ver_tokens.config(state="disabled")
        boton_ver_tablas.config(state="disabled")


def analizar_archivo():
    if not entry_archivo.get():
        return
    try :
        with open(entry_archivo.get(), "r") as f:
            pass
    except:
        #Show an error box
        messagebox.showerror("Error", "El archivo no existe")   

    resultado = main.analizar_gui(entry_archivo.get())
    exito = resultado[1]
    if exito:
        boton_ver_arbol.config(state="normal")
        boton_ver_tokens.config(state="normal")
        boton_ver_tablas.config(state="normal")
    caja_texto.config(state="normal")
    caja_texto.delete("1.0", tk.END)
    caja_texto.insert("1.0", resultado[0])
    caja_texto.config(state="disabled")
    

def ver_arbol():
    ruta_arbol = "parse.txt"
    abrir_archivo(ruta_arbol)

def ver_tokens():
    ruta_tokens = "tokens.txt"
    abrir_archivo(ruta_tokens)

def ver_tablas():
    ruta_tablas = "tablas.txt"
    abrir_archivo(ruta_tablas)

def ver_codigo():
    abrir_archivo(entry_archivo.get())

def abrir_archivo(ruta):
    try:
        subprocess.Popen([ruta], shell=True)
    except:
        messagebox.showerror("Error", f"No se ha podido abrir el archivo {ruta}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Analizador Sintáctico Ascendente LR(1)")

# Fila 1: Seleccionar Archivo y Analizar
label_archivo = ttk.Label(ventana, text="Archivo:")
label_archivo.grid(row=0, column=0, padx=5, pady=5)

entry_archivo = ttk.Entry(ventana, width=20, state="readonly")
entry_archivo.grid(row=0, column=1, padx=5, pady=5)

boton_seleccionar = ttk.Button(ventana, text="Abrir Archivo", command=seleccionar_archivo)
boton_seleccionar.grid(row=0, column=2, padx=5, pady=5)

boton_analizar = ttk.Button(ventana, text="Analizar", command=analizar_archivo, state="disabled")
boton_analizar.grid(row=0, column=3, padx=5, pady=5)

# Fila 2: Caja de Texto
label_resultado = ttk.Label(ventana, text="Resultado:")
label_resultado.grid(row=1, column=0, padx=5, pady=5)

caja_texto = tk.Text(ventana, height=5, width=50, state="disabled")
caja_texto.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

# Fila 3: Ver Árbol y Ver Tokens
boton_ver_codigo = ttk.Button(ventana, text="Ver Código", command=ver_codigo, state="disabled")
boton_ver_codigo.grid(row=2, column=0,columnspan=1,  padx=5, pady=5)

boton_ver_arbol = ttk.Button(ventana, text="Ver Árbol", command=ver_arbol, state="disabled")
boton_ver_arbol.grid(row=2, column=1,columnspan=1,  padx=5, pady=5)

boton_ver_tokens = ttk.Button(ventana, text="Ver Tokens", command=ver_tokens, state="disabled")
boton_ver_tokens.grid(row=2, column=2,columnspan=1,  padx=5, pady=5)

boton_ver_tablas = ttk.Button(ventana, text="Ver Tablas", command=ver_tablas, state="disabled")
boton_ver_tablas.grid(row=2, column=3,columnspan=1,  padx=5, pady=5)


# Ejecutar la aplicación
ventana.mainloop()
