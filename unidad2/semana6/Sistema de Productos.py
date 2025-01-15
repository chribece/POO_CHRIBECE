# Clase base: Producto
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre  # Encapsulación: atributo protegido
        self._precio = precio  # Encapsulación: atributo protegido

    # Metodo para obtener el nombre (getter)
    def get_nombre(self):
        return self._nombre

    # Metodo para obtener el precio (getter)
    def get_precio(self):
        return self._precio

    #Metodo para mostrar información del producto
    def mostrar_informacion(self):
        return f"Producto: {self._nombre}, Precio: ${self._precio}"

    # Método polimórfico (puede ser sobrescrito en clases derivadas)
    def calcular_descuento(self, descuento):
        return self._precio * (1 - descuento)


# Clase derivada: ProductoElectronico (hereda de Producto)
class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, garantia):
        super().__init__(nombre, precio)  # Llama al constructor de la clase base
        self.__garantia = garantia  # Encapsulación: atributo privado

    # Metodo para obtener la garantía (getter)
    def get_garantia(self):
        return self.__garantia

    # Sobrescritura del metodo mostrar_informacion
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Garantía: {self.__garantia} meses"

    # Sobrescritura del metodo calcular_descuento (polimorfismo)
    def calcular_descuento(self, descuento):
        return super().calcular_descuento(descuento) - 10  # Descuento adicional para productos electrónicos


# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias de las clases
    producto_general = Producto("Lápiz", 5)
    producto_electronico = ProductoElectronico("Smartphone", 1000, 12)

    # Mostrar información de los productos
    print(producto_general.mostrar_informacion())  # Salida: Producto: Lápiz, Precio: $5
    print(producto_electronico.mostrar_informacion())  # Salida: Producto: Smartphone, Precio: $1000, Garantía: 12 meses

    # Calcular descuentos (polimorfismo)
    print(f"Precio con descuento (Lápiz): ${producto_general.calcular_descuento(0.1):.2f}")  # Salida: Precio con descuento (Lápiz): $4.50
    print(f"Precio con descuento (Smartphone): ${producto_electronico.calcular_descuento(0.1):.2f}")  # Salida: Precio con descuento (Smartphone): $890.00

    # Acceder a atributos encapsulados (usando getters)
    print(f"Nombre del producto electrónico: {producto_electronico.get_nombre()}")  # Salida: Nombre del producto electrónico: Smartphone
    print(f"Garantía del producto electrónico: {producto_electronico.get_garantia()} meses")  # Salida: Garantía del producto electrónico: 12 meses