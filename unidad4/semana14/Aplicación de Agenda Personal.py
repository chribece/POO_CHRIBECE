import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Importamos DateEntry para el selector de fecha
import datetime  # Importa el módulo datetime para manejar fechas y horas


# Clase principal
class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        # Configuración de estilo
        self.style = ttk.Style()
        self.style.configure("Treeview", font=('Arial', 10))
        self.style.configure("TButton", font=('Arial', 10))
        self.style.configure("TLabel", font=('Arial', 10))
        self.style.configure("Yellow.TFrame", background="#fdc307")

        # Creamos los frames para organizar la interfaz
        self.crear_frames()

        # Creamos los componentes de la interfaz
        self.crear_componentes_visualizacion()
        self.crear_componentes_entrada()
        self.crear_componentes_acciones()

        # Lista para almacenar eventos (podría reemplazarse por una base de datos en una aplicación real)
        self.eventos = []

    # Crea los frames para organizar la interfaz
    def crear_frames(self):
        # Frame para visualizar eventos
        self.frame_visualizacion = ttk.Frame(self.root, padding="10", style="Yellow.TFrame")
        self.frame_visualizacion.pack(fill=tk.BOTH, expand=True)

        # Frame para entrada de datos
        self.frame_entrada = ttk.Frame(self.root, padding="10")
        self.frame_entrada.pack(fill=tk.X)

        # Frame para botones de acción
        self.frame_acciones = ttk.Frame(self.root, padding="10")
        self.frame_acciones.pack(fill=tk.X)

    def crear_componentes_visualizacion(self):
        titulo_frame = tk.Frame(self.frame_visualizacion, bg="#fdc307")
        titulo_frame.pack(fill=tk.X)

        # Etiqueta para la sección de visualización centrada
        tk.Label(titulo_frame, text="Eventos", font=('Arial', 12, 'bold'), bg="#fdc307").pack(
            anchor=tk.CENTER, expand=True)

        # Crear un frame para contener el Treeview y scrollbars
        contenido_frame = tk.Frame(self.frame_visualizacion, bg="#fdc307")
        contenido_frame.pack(fill=tk.BOTH, expand=True)

        # Crear el Treeview para mostrar los eventos
        self.tree = ttk.Treeview(contenido_frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        # Configurar el ancho de las columnas
        self.tree.column("Fecha", width=100)
        self.tree.column("Hora", width=100)
        self.tree.column("Descripción", width=500)

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

    def crear_componentes_entrada(self):
        # Crear un sub-frame para organizar los componentes de entrada
        entrada_form = ttk.Frame(self.frame_entrada)
        entrada_form.pack(fill=tk.X, padx=5, pady=5)

        # Etiqueta y selector de fecha
        ttk.Label(entrada_form, text="Fecha:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.fecha_selector = DateEntry(entrada_form, width=12, background='darkblue',
                                        foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.fecha_selector.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        # Etiqueta y entrada para la hora
        ttk.Label(entrada_form, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.hora_var = tk.StringVar()
        self.hora_entry = ttk.Entry(entrada_form, textvariable=self.hora_var, width=8)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)

        # Etiqueta y entrada para la descripción
        ttk.Label(entrada_form, text="Descripción:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.descripcion_var = tk.StringVar()
        self.descripcion_entry = ttk.Entry(entrada_form, textvariable=self.descripcion_var, width=60)
        self.descripcion_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky=tk.W + tk.E)

        # Hacer que la columna de descripción sea expandible
        entrada_form.columnconfigure(3, weight=1)

    def crear_componentes_acciones(self):
        # Botón para agregar evento
        self.btn_agregar = ttk.Button(self.frame_acciones, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.pack(side=tk.LEFT, padx=5)

        # Botón para eliminar evento
        self.btn_eliminar = ttk.Button(self.frame_acciones, text="Eliminar Evento",
                                       command=self.eliminar_evento)
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)

        # Botón para salir
        self.btn_salir = ttk.Button(self.frame_acciones, text="Salir", command=self.root.quit)
        self.btn_salir.pack(side=tk.RIGHT, padx=5)

    def agregar_evento(self):
        # Obtener los datos de los campos de entrada
        try:
            fecha = self.fecha_selector.get_date().strftime("%d/%m/%Y")
            hora = self.hora_var.get()
            descripcion = self.descripcion_var.get()

            # Validar que los campos no estén vacíos
            if not hora or not descripcion:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")
                return

            # Validar formato de hora (HH:MM)
            if not self.validar_hora(hora):
                messagebox.showerror("Error", "Formato de hora incorrecto. Use HH:MM")
                return

            # Añadir el evento a la lista y al Treeview
            evento = (fecha, hora, descripcion)
            self.eventos.append(evento)
            self.tree.insert("", tk.END, values=evento)

            # Limpiar los campos de entrada
            self.limpiar_campos()

            messagebox.showinfo("Éxito", "Evento agregado correctamente.")

        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")

    def eliminar_evento(self):
        # Verificar si hay un elemento seleccionado
        item_seleccionado = self.tree.selection()

        if not item_seleccionado:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un evento para eliminar.")
            return

        # Mostrar diálogo de confirmación
        respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este evento?")

        if respuesta:
            # Obtener los valores del elemento seleccionado
            valores = self.tree.item(item_seleccionado)['values']

            # Eliminar de la lista de eventos
            if valores in self.eventos:
                self.eventos.remove(valores)

            # Eliminar del Treeview
            self.tree.delete(item_seleccionado)

            messagebox.showinfo("Éxito", "Evento eliminado correctamente.")

    def limpiar_campos(self):
        # Establecer la fecha a hoy
        self.fecha_selector.set_date(datetime.datetime.now())
        # Limpiar los otros campos
        self.hora_var.set("")
        self.descripcion_var.set("")

    def validar_hora(self, hora):
        """
        Valida que la hora tenga el formato HH:MM
        """
        try:
            # Intentar convertir la hora a un objeto de hora
            datetime.datetime.strptime(hora, "%H:%M")
            return True
        except ValueError:
            return False


# Función para iniciar la aplicación
def main():
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()


if __name__ == "__main__":
    main()