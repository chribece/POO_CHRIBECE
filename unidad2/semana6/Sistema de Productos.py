#Importar biblioteca para crear tablas
from tabulate import tabulate  #

# Clase padre constructor
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # Metodo para obtener el nombre (getter)
    def get_nombre(self):
        return self.nombre

    # Metodo para obtener el precio (getter)
    def get_precio(self):
        return self.precio

    # Metodo  mostrar información del producto
    def mostrar_informacion(self):
        return [self.nombre, f"${self.precio}", "N/A"]

    # Metodo polimórfico calcular descuento
    def calcular_descuento(self, descuento):
        return self.precio * (1 - descuento)

# Clase hija  ProductoElectronico (hereda de Producto)
class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, garantia):
        super().__init__(nombre, precio)  # Llama al constructor de la clase padre
        # Encapsulación: atributo privado
        self.__garantia = garantia

    # Metodo para obtener la garantía (getter)
    def get_garantia(self):
        return self.__garantia

    # Sobrescritura del metodo mostrar_informacion
    def mostrar_informacion(self):
        return [self.nombre, f"${self.precio}", f"{self.__garantia} meses"]

    # Sobrescritura del metodo calcular_descuento (polimorfismo)
    def calcular_descuento(self, descuento):
        return super().calcular_descuento(descuento) - 10  # Descuento adicional para productos electrónicos


# Función para mostrar una tabla de productos
def mostrar_tabla(productos):
    # Encabezados de la tabla
    headers = ["Nombre", "Precio", "Garantía"]
    # Lista para almacenar los datos de los productos
    tabla = []

    for producto in productos:
        # Agregar información del producto a la tabla
        tabla.append(producto.mostrar_informacion())
        # Mostrar la tabla
    print(tabulate(tabla, headers, tablefmt="pretty"))


# Menú interactivo
def menu():
    productos = []  # Lista para almacenar los productos

    while True:
        print("\n--- Menú del Sistema de Productos ---")
        print("1. Agregar producto general")
        print("2. Agregar producto electrónico")
        print("3. Mostrar todos los productos")
        print("4. Calcular descuento para un producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Agregar producto general
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(nombre, precio)
            productos.append(producto)
            print(f"Producto '{nombre}' agregado correctamente.")

        elif opcion == "2":
            # Agregar producto electrónico
            nombre = input("Ingrese el nombre del producto electrónico: ")
            precio = float(input("Ingrese el precio del producto electrónico: "))
            garantia = int(input("Ingrese la garantía (en meses): "))
            producto = ProductoElectronico(nombre, precio, garantia)
            productos.append(producto)
            print(f"Producto electrónico '{nombre}' agregado correctamente.")

        elif opcion == "3":
            # Mostrar todos los productos en una tabla
            if not productos:
                print("No hay productos registrados.")
            else:
                print("\n--- Lista de Productos ---")
                mostrar_tabla(productos)

        elif opcion == "4":
            # Calcular descuento para un producto
            if not productos:
                print("No hay productos registrados.")
            else:
                print("\n--- Calcular Descuento ---")
                for i, producto in enumerate(productos):
                    print(f"{i + 1}. {producto.get_nombre()}")
                seleccion = int(input("Seleccione el número del producto: ")) - 1

                if 0 <= seleccion < len(productos):
                    descuento = float(input("Ingrese el porcentaje de descuento (ejemplo: 0.1 para 10%): "))
                    precio_final = productos[seleccion].calcular_descuento(descuento)
                    print(f"Precio con descuento: ${precio_final:.2f}")
                else:
                    print("Selección inválida.")

        elif opcion == "5":
            # Salir del programa
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutar el menú
if __name__ == "__main__":
    menu()