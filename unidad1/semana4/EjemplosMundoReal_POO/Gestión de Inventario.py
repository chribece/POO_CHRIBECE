#Clase producto que se representa en el invenario
class producto:
    #Metodo constructor
    def __init__(self, nombre, precioc,preciov, cantidad):
        self.nombre = nombre
        self.precioc = precioc
        self.preciov = preciov
        self.cantidad = cantidad
    #Metodo mostrar producto
    def mostrar(self):
        print(f"Producto: {self.nombre:<15} | Precio de Compra: ${self.precioc:<7} | Precio de Venta: ${self.preciov:<7} | Cantidad: {self.cantidad:<5}")

    # Metodo actualizar cantidad disponible producto
    def actualizar_cantidad(self,cantidad):
        self.cantidad += cantidad
        print(f"Cantidad de {self.nombre} actualizada a {self.cantidad}")

#Clase inventario de productos
class inventario:
    #metodo constructor
    def __init__(self):
        self.productos = [] #lista que almacena los productos
    #Metodo agregar producto al inventario
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto: {producto.nombre} agregado al inventario")

    #Metodo eliminar producto del inventario
    def eliminar_producto(self, nombre_producto):
        self.productos = [producto for producto in self.productos if producto.nombre != nombre_producto]
        print(f"Producto: {nombre_producto} eliminado del inventario")

    #Metodo buscar producto por nombre del inventario
    def buscar_producto(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                return producto
        return None

    #Metodo mostrar todos los producto del inventario
    def mostrar_productos(self):
        if not self.productos:
            print("El inventario se encuentra vacío")
        else:
            print("Inventario:")
            print(f"{'Producto':<25} | {'Precio compra':<26} | {'Precio de Venta':<25} | {'Cantidad':<10}")
            print("-"*40)
            for producto in self.productos:
                producto.mostrar()
#Funcion menu
def menu():
    print("\nGESTION DE INVENTARIO REPUESTOS AUTOMOTRICES")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Buscar producto")
    print("4. Actualizar productos")
    print("5. Mostrar producto")
    print("6. Salir")


if __name__ == "__main__":
    inventario_obj = inventario()
    while True:
        menu()
        opcion=input("Seleccione una opcion: ")

        if opcion == "1":
            nombre=input("Nombre del producto: ")
            precioc=float(input("Precio de compra del producto: "))
            preciov=float(input("Precio de venta del producto: "))
            cantidad=int(input("Cantidad: "))
            nuevo_producto=producto(nombre,precioc,preciov,cantidad)
            inventario_obj.agregar_producto(nuevo_producto)

        elif opcion == "2":
            nombre=input("Nombre del producto a eliminar: ")
            inventario_obj.eliminar_producto(nombre)

        elif opcion == "3":
            nombre=input("Nombre del producto a buscar: ")
            producto_encontrado=inventario_obj.buscar_producto(nombre)
            if producto_encontrado:
                print("Producto: ")
                producto_encontrado.mostrar()
            else:
                print(f"Producto: {nombre} no encontrado")

        elif opcion == "4":
            nombre=input("Nombre del producto: ")
            producto_encontrado=inventario_obj.buscar_producto(nombre)
            if producto_encontrado:
                cantidad=int(input("Cantidad: "))
                producto_encontrado.actualizar_cantidad(cantidad)
            else:
                print(f"Producto: {nombre} no encontrado")

        elif opcion == "5":
            inventario_obj.mostrar_productos()

        elif opcion == "6":
            print("Salir")
            break
        else:
            print("Opcion invalida. Intente nuevamente")

