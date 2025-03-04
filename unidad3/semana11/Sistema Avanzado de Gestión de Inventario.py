#Importa módulo que incluye funciones para interactuar con el sistema de archivos
import os
import json

#Importa biblioteca para crear tablas
from tabulate import tabulate

#Programa para la gestion de inventario de una tienda

#Clase Producto
class Producto:
#constructor
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
#Metodos guetters
    def get_id(self):
        return self.id
    def get_nombre(self):
        return self.nombre
    def get_cantidad(self):
        return self.cantidad
    def get_precio(self):
        return self.precio
#metodos setters
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.cantidad = cantidad
        else:
            print("Error: La cantidad no puede ser negativa")

    def set_precio(self, precio):
        self.precio = precio
    def __str__(self):
        return f"ID: {self.id:<15} | Nombre Producto: {self.nombre:<15} | Cantidad: {self.cantidad:<7} | Precio: ${self.precio:<7} "

# metodo para compartir el producto a un diccionario (JSON)
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }
# Metodo de clase para crear un producto desde un diccionario
    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["nombre"], data["cantidad"], data["precio"])

#Clase inventario
class Inventario:
    #metodo constructor
    def __init__(self):
        #Diccionario de productos
        self.productos = {}
        #Archivo donde se almacenara el inventario json
        self.archivo_inventario="inventario.json"
        #Carga el inventario existente al iniciar
        self.cargar_inventario()

    #Metodo cargar inventario
    def cargar_inventario(self):

        #Carga el inventario iniciar el programa

        #Inicio un bloque de manejo de excepciones
        try:
            #Verifica si el archivo de inventario existe
            if os.path.exists(self.archivo_inventario):
                #Abre el archivo en modo lectura
                with open(self.archivo_inventario, "r") as f:
                    datos = json.load(f)
                    # Convierte cada entrada del diccionario en un objeto Producto
                    self.productos = {int(id):Producto.from_dict(info) for id, info in datos.items()}
                print("Inventario cargado desde el archivo")
            else:
                # Crear archivo si no existe
                with open(self.archivo_inventario, "w") as f:
                    json.dump({}, f)
                print("Archivo Inventario creado")
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error al cargar el inventario: {str(e)}")
            # Asegura que el diccionario esté inicializado incluso si falla
            self. productos = {}
#Metodo guardar inventario
    def guardar_inventario(self):
    #Guarda el inventario actual en el archivo
        try:
            with open(self.archivo_inventario, "w") as f:
                #Convierte los productos a diccionarios y usa el ID como clave
                datos = {str(producto.get_id()): producto.to_dict() for producto in self.productos.values()}
                json.dump(datos, f, indent=4)
            print("Cambios guardados en el archivo JSON correctamente")
        except PermissionError:
            print("No tiene permiso para escribir en el archivo")
        except Exception as e:
            print(f"Error al guardar el inventario: {str(e)}")

#Metodo agregar producto
    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Ya existe el producto")
            return False
        self.productos[producto.get_id()] = producto
        self.guardar_inventario()
        print(f"Producto: {producto.get_nombre()} agregado al inventario exitosamente")
        return True

#Metodo eliminar producto
    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            print(f"Producto eliminado del inventario exitosamente")
            return True
        print("No se encuentra el producto")
        return False


#Metodo actualizar producto
    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            self.guardar_inventario()
            print("Producto actualizado exitosamente")
            return True
        print("No se encuentra el producto")
        return False

#Metodo buscar producto
    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
            return True
        print("No se encuentra el producto")
        return False

#Metodo mostrar productos
    def mostrar_productos(self):
        if self.productos:
            self.mostrar_tabla(self.productos.values())
        else:
            print("Inventario vacío")

    def mostrar_tabla(self, productos):
        tabla=[]
        for producto in productos:
            fila=[
                producto.get_id(),
                producto.get_nombre(),
                producto.get_cantidad(),
                f"${producto.get_precio():.2f}"
            ]
            tabla.append(fila)
        headers = ["ID", "Nombre", "Cantidad", "Precio"]
        print(tabulate(tabla, headers=headers, tablefmt="pretty"))


def menu():
    inventario=Inventario()
    while True:
        print("\n--- MENU GESTION DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar productos")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion=input("Seleccione una opcion: ")

        if opcion == "1":
            try:
                id=int(input("Ingrese el ID del producto: "))
                nombre=input("Ingrese el nombre del producto: ")
                cantidad=int(input("Ingrese el cantidad del producto: "))
                precio=float(input("Ingrese el precio del producto: "))
                producto = Producto(id, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: Por favor ingrese valores numéricos válidos")

        elif opcion == "2":
            try:
                id=int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id)
            except ValueError:
                print("Error: El ID debe ser un número entero")

        elif opcion == "3":
            try:
                id=int(input("Ingrese el id del producto a actualizar: "))
                cantidad=input("Ingrese el cantidad del producto (Enter para omitir): ")
                precio=input("Ingrese el precio del producto (Enter para omitir): ")
                cantidad=int(cantidad) if cantidad else None
                precio=float(precio) if precio else None
                inventario.actualizar_producto(id, cantidad, precio)
            except ValueError:
                print("Error: Por favor ingrese valores numéricos válidos")

        elif opcion == "4":
            nombre=input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Salir")
            break
        else:
            print("Opcion invalida")
if __name__ == "__main__":
    menu()

