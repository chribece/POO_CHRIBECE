#Importar biblioteca para crear tablas
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


#clase inventario
class Inventario:
#metodo constructor
    def __init__(self):
#Lista productos
        self.productos = []
#Metodo agregar producto
    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Ya existe el producto")
        else:
            self.productos.append(producto)
            print(f"Producto: {producto.nombre} agregado al inventario")
#Metodo eliminar producto
    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                print(f"Producto eliminado del inventario")
                return
        print("No se encuentra el producto")

#Metodo actualizar producto
    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print(f"Producto actualizado")
                return
        print("No se encuentra el producto")

#Metodo buscar producto
    def buscar_producto(self, nombre):
        resultados=[p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encuentra el producto")
#Metodo mostrar productos
    def mostrar_productos(self):
        if self.productos:
            self.mostrar_tabla(self.productos)
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
            id=int(input("Ingrese el id del producto: "))
            nombre=input("Ingrese el nombre del producto: ")
            cantidad=int(input("Ingrese el cantidad del producto: "))
            precio=float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            id=int(input("Ingrese el id del producto a eliminar: "))
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id=int(input("Ingrese el id del producto a actualizar: "))
            cantidad=input("Ingrese el cantidad del producto: ")
            precio=input("Ingrese el precio del producto: ")
            cantidad=int(cantidad) if cantidad else None
            precio=float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
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

