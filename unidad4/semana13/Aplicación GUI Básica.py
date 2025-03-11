# Importamos la librería tkinter
import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
aplicacionGUI=tk.Tk()
aplicacionGUI.geometry('400x300')
aplicacionGUI.title("Aplicación GUI Básica")
aplicacionGUI.configure(background='green')

# Configurar tabla
aplicacionGUI.columnconfigure(0, weight=1)
aplicacionGUI.columnconfigure(1, weight=1)
aplicacionGUI.rowconfigure(0, weight=0)
aplicacionGUI.rowconfigure(1, weight=1)
aplicacionGUI.rowconfigure(2, weight=0)

# Etiqueta
label_nombre=ttk.Label(aplicacionGUI, text="Ingresa tu nombre:")
label_nombre.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

# Campo de texto
entrada_texto=ttk.Entry(aplicacionGUI)
entrada_texto.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

# Mostrar items en una lista
lista_items=tk.Listbox(aplicacionGUI,height=10,width=50)
lista_items.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))

# Funcion agregar
def agregar_lista():
    texto=entrada_texto.get().strip()
    if texto and texto not in lista_items.get(0, tk.END):
        lista_items.insert(tk.END, texto)
        entrada_texto.delete(0, tk.END)
# Funcion limpiar
def limpiar_lista():
    lista_items.delete(0, tk.END)

# Botón agregar
boton_agregar= ttk.Button(aplicacionGUI, text="Agregar", command=agregar_lista)
boton_agregar.grid(row=2, column=0, padx=5, pady=5)

# Botón limpiar
boton_limpiar=ttk.Button(aplicacionGUI, text="Limpiar", command=limpiar_lista)
boton_limpiar.grid(row=2, column=1, padx=5, pady=5)

# Inicio aplicacion
aplicacionGUI.mainloop()