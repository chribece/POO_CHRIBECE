import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Importamos DateEntry para el selector de fecha
import datetime  # Importa el módulo datetime para manejar fechas y horas

# Clase principal
class ListaTareas:
    #Constructor inicializa la ventana principal
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("800x600")
        self.root.iconbitmap("gf.ico")
        self.root.resizable(True, True)

        # Configuración de estilo
        self.style = ttk.Style()
        self.style.configure("Treeview", font=('Arial', 10))
        self.style.configure("TButton", font=('Arial', 10))
        self.style.configure("TLabel", font=('Arial', 10))
        self.style.configure("Visualizacion.TFrame", background="#1c1c91")
        self.style.configure("Entrada.TFrame", background="#ffbe00")
        self.style.configure("Acciones.TFrame", background="#1c1c91")

        # Llamada a los metodos de la interfaz
        self.crear_frames()
        self.crear_componentes_visualizacion()
        self.crear_componentes_entrada()
        self.crear_componentes_acciones()

        # Lista para almacenar tareas
        self.tareas = []

        # Evento vincular la tecla Enter al metodo agregar_tarea
        self.root.bind('<Return>', lambda event: self.agregar_tarea())

    # Metodo para crear los contenedores principales
    def crear_frames(self):
        self.frame_visualizacion = ttk.Frame(self.root, padding="10", style="Visualizacion.TFrame")
        self.frame_visualizacion.pack(fill=tk.BOTH, expand=True)

        # Frame para entrada de datos
        self.frame_entrada = ttk.Frame(self.root, padding="10", style="Entrada.TFrame")
        self.frame_entrada.pack(fill=tk.X)

        # Frame para botones de acción
        self.frame_acciones = ttk.Frame(self.root, padding="10", style="Acciones.TFrame")
        self.frame_acciones.pack(fill=tk.X)

    # Metodo para crear la sección de visualización de tareas
    def crear_componentes_visualizacion(self):
        titulo_frame = tk.Frame(self.frame_visualizacion, bg="#fdc307")
        titulo_frame.pack(fill=tk.X)

        # Etiqueta para la sección de visualización centrada
        tk.Label(titulo_frame, text="Tareas", font=('Arial', 12, 'bold'), bg="#fdc307").pack(
            anchor=tk.CENTER, expand=True)

        # Crear un frame para contener el Treeview y scrollbars
        contenido_frame = tk.Frame(self.frame_visualizacion, bg="#fdc307")
        contenido_frame.pack(fill=tk.BOTH, expand=True)

        # Modificamos las columnas para incluir estado
        self.tree = ttk.Treeview(contenido_frame,
                                 columns=("Fecha", "Tarea", "Estado"),
                                 show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Tarea", text="Tarea")
        self.tree.heading("Estado", text="Estado")
        # Configurar el ancho de las columnas
        self.tree.column("Fecha", width=100)
        self.tree.column("Tarea", width=500)
        self.tree.column("Estado", width=100)
        # Añadir scrollbars
        scrollbar_y = ttk.Scrollbar(contenido_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar_x = ttk.Scrollbar(contenido_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        # Posicionar el Treeview y scrollbars
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar_y.grid(row=0, column=1, sticky="ns")
        scrollbar_x.grid(row=1, column=0, sticky="ew")
        # Configurar el contenido_frame para que sea expandible
        contenido_frame.columnconfigure(0, weight=1)
        contenido_frame.rowconfigure(0, weight=1)

        # Evento doble clic para toggle estado
        self.tree.bind("<Double-1>", self.toggle_estado)

        # Metodo para crear los campos de entrada
    def crear_componentes_entrada(self):
        entrada_form = ttk.Frame(self.frame_entrada)
        entrada_form.pack(fill=tk.X, padx=5, pady=5)

        # Etiqueta y selector de fecha
        ttk.Label(entrada_form, text="Fecha:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.fecha_selector = DateEntry(entrada_form, width=12, background='darkblue',
                                        foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.fecha_selector.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        # Etiqueta y entrada de  la tarea
        ttk.Label(entrada_form, text="Tarea:").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.tarea_var = tk.StringVar()
        self.tarea_entry = ttk.Entry(entrada_form, textvariable=self.tarea_var, width=50)
        self.tarea_entry.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W + tk.E)

        # Hacer que la columna de descripción sea expandible
        entrada_form.columnconfigure(3, weight=1)

    # Metodo para acciones en botón para agregar tarea
    def crear_componentes_acciones(self):
        self.btn_agregar = ttk.Button(self.frame_acciones, text="Agregar Tarea", command=self.agregar_tarea)
        self.btn_agregar.pack(side=tk.LEFT, padx=5)
        # Botón para eliminar tarea
        self.btn_eliminar = ttk.Button(self.frame_acciones, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)
        # Botón para salir
        self.btn_salir = ttk.Button(self.frame_acciones, text="Salir", command=self.root.quit)
        self.btn_salir.pack(side=tk.RIGHT, padx=5)

    def agregar_tarea(self):
        # Obtener los datos de los campos de entrada
        try:
            fecha = self.fecha_selector.get_date().strftime("%d/%m/%Y")
            tarea = self.tarea_var.get()
            # Validar que los campos no estén vacíos
            if not tarea:
                messagebox.showerror("Error", "Por favor, ingrese una tarea.")
                return

            tarea_nueva = (fecha, tarea, "Pendiente")
            self.tareas.append(tarea_nueva)
            self.tree.insert("", tk.END, values=tarea_nueva)
            # Limpiar los campos de entrada
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Tarea agregada correctamente.")

        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")

    def eliminar_tarea(self):
        # Verificar si hay un elemento seleccionado
        item_seleccionado = self.tree.selection()
        if not item_seleccionado:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para eliminar.")
            return
        # Mostrar diálogo de confirmación
        respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar esta tarea?")
        # Obtener los valores del elemento seleccionado
        if respuesta:
            valores = self.tree.item(item_seleccionado)['values']
            if tuple(valores) in self.tareas:
                self.tareas.remove(tuple(valores))
                # Eliminar del Treeview
            self.tree.delete(item_seleccionado)
            messagebox.showinfo("Éxito", "Tarea eliminada correctamente.")

    # metodo que cambia entre "Pendiente" y "Completada" con doble clic
    def toggle_estado(self, event):
        item_seleccionado = self.tree.selection()
        if not item_seleccionado:
            return

        valores = list(self.tree.item(item_seleccionado)['values'])
        indice = self.tareas.index(tuple(valores))

        # Cambiar estado
        if valores[2] == "Pendiente":
            valores[2] = "Completada"
        else:
            valores[2] = "Pendiente"

        # Actualizar lista y Treeview
        self.tareas[indice] = tuple(valores)
        self.tree.item(item_seleccionado, values=valores)

    def limpiar_campos(self):
        self.fecha_selector.set_date(datetime.datetime.now())
        self.tarea_var.set("")


def main():
    root = tk.Tk()
    app = ListaTareas(root)
    root.mainloop()


if __name__ == "__main__":
    main()