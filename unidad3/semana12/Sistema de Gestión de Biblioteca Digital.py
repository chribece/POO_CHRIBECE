import json
from datetime import datetime

#Clase Libro
class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str, categoria: str, prestado: bool=False ):
        #Usamos una tupla para almacenar titulo y autor (inmutable)
        self._inf_basica=(titulo, autor)
        self.isbn = isbn
        self.categoria = categoria
        self.prestado = prestado

# Propiedades para acceder a los atributos inmutables
    @property
    def titulo(self):
        return self._inf_basica[0]

    @property
    def autor(self):
        return self._inf_basica[1]

#Convierte el libro a un diccionario para guardar en JSON

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "prestado": self.prestado

        }
# Crea un libro desde un diccionario
    @classmethod
    def from_dict(cls, data):
        return cls(data["isbn"], data["titulo"], data["autor"], data["categoria"], data["prestado"])

# Crea clase usuario
class Usuario:
    def __init__(self, user_id:str, nombre:str):
        self.user_id = user_id
        self.nombre = nombre
        #lista para almacenar libros prestados
        self.libros_prestados=[]

    # Convierte el usuario a un diccionario para guardar en JSON
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "nombre": self.nombre,
            "libros_prestados":[libro.isbn for libro in self.libros_prestados]
        }

    # Crea un usuario desde un diccionario
    @classmethod
    def from_dict(cls, data):
        return cls(data["user_id"], data["nombre"])

# Clase Biblioteca
class Biblioteca:
    def __init__(self, archivo_json='biblioteca.json'):
        self.archivo_json=archivo_json
        # Diccionario para libros (ISBN: Libro)
        self.libros={}
        # Diccionario para usuarios (user_id: Usuario)
        self.usuarios={}
        # Conjunto para IDs únicos de usuarios
        self.usuarios_ids=set()
        # Lista para el historial de préstamos
        self.historial=[]
        self.cargar_datos()

    #Carga los datos desde el archivo JSON
    def cargar_datos(self):
        try:
            with open(self.archivo_json, 'r') as archivo:
                datos = json.load(archivo)
                # Cargar libros
                self.libros= {isbn:Libro.from_dict(info) for isbn, info in datos.get("libros",{}).items()}
                # Cargar libros
                self.usuarios={uid:Usuario.from_dict(info) for uid, info in datos.get("usuarios",{}).items()}
                self.usuarios_ids=set(self.usuarios.keys())
                # Restaurar libros prestados
                for uid, usuario in self.usuarios.items():
                    for isbn in usuario.to_dict()["libros_prestados"]:
                        if isbn in self.libros:
                            usuario.libros_prestados.append(self.libros[isbn])
        # Cargar historial
                self.historial=datos.get("historial",[])
        except(FileNotFoundError, json.JSONDecodeError):
            print("No se encontró archivo.")

    #Guarda todos los datos en el archivo JSON
    def guardar_datos(self):

        datos = {
            "libros": {isbn: libro.to_dict() for isbn, libro in self.libros.items()},
            "usuarios": {uid: usuario.to_dict() for uid, usuario in self.usuarios.items()},
            "historial": self.historial
        }
        with open(self.archivo_json, 'w') as archivo:
            json.dump(datos, archivo, indent=4)

    #Añade un libro si el ISBN no existe
    def añadir_libro(self, libro: Libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            self.guardar_datos()
            print(f"Libro '{libro.titulo}' añadido con éxito")
        else:
            print("Ya existe un libro con ese ISBN")

    #Elimina un libro si no está prestado
    def quitar_libro(self, isbn: str):
        if isbn in self.libros and not self.libros[isbn].prestado:
            del self.libros[isbn]
            self.guardar_datos()
            print("Libro eliminado con éxito")
        else:
            print("El libro no existe o está prestado")

    #Registra un usuario si el ID no existe
    def registrar_usuario(self, usuario: Usuario):
        if usuario.user_id not in self.usuarios_ids:
            self.usuarios_ids.add(usuario.user_id)
            self.usuarios[usuario.user_id] = usuario
            self.guardar_datos()
            print(f"Usuario '{usuario.nombre}' registrado con éxito")
        else:
            print("El ID de usuario ya existe")

    #Elimina un usuario si no tiene libros prestados
    def dar_baja_usuario(self, user_id: str):
        if user_id in self.usuarios and not self.usuarios[user_id].libros_prestados:
            del self.usuarios[user_id]
            self.usuarios_ids.remove(user_id)
            self.guardar_datos()
            print("Usuario eliminado con éxito")
        else:
            print("El usuario no existe o tiene libros prestados")

    #Presta un libro a un usuario
    def prestar_libro(self, isbn: str, user_id: str):
        if isbn in self.libros and user_id in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[user_id]
            if not libro.prestado:
                libro.prestado = True
                usuario.libros_prestados.append(libro)
                self.historial.append({
                    "user_id": user_id,
                    "isbn": isbn,
                    "fecha": datetime.now().isoformat()
                })
                self.guardar_datos()
                print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}")
            else:
                print("El libro ya está prestado")
        else:
            print("Libro o usuario no encontrado")

    #Devuelve un libro prestado por un usuario
    def devolver_libro(self, isbn: str, user_id: str):
        if isbn in self.libros and user_id in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[user_id]
            if libro in usuario.libros_prestados:
                libro.prestado = False
                usuario.libros_prestados.remove(libro)
                self.guardar_datos()
                print(f"Libro '{libro.titulo}' devuelto con éxito")
            else:
                print("El libro no está prestado a este usuario")
        else:
            print("Libro o usuario no encontrado")

    #Busca libros por título, autor o categoría
    def buscar_libros(self, termino: str, criterio: str = "titulo"):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and termino.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and termino.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and termino.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    #Muestra los libros prestados a un usuario
    def listar_libros_prestados(self, user_id: str):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(f"- {libro.titulo} por {libro.autor}")
            else:
                print("No hay libros prestados a este usuario")
        else:
            print("Usuario no encontrado")

    # Muestra todos los libros disponibles
    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía")
        else:
            for libro in self.libros.values():
                estado = "Prestado" if libro.prestado else "Disponible"
                print(f"{libro.isbn}: {libro.titulo} por {libro.autor} - {estado}")

def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n=== Sistema de Biblioteca Digital ===")
        print("1. Añadir Libro")
        print("2. Quitar Libro")
        print("3. Registrar Usuario")
        print("4. Dar de baja Usuario")
        print("5. Prestar Libro")
        print("6. Devolver Libro")
        print("7. Buscar Libros")
        print("8. Listar Libros Prestados")
        print("9. Mostrar Todos los Libros")
        print("10. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.añadir_libro(libro)

        elif opcion == '2':
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == '3':
            user_id = input("ID de usuario: ")
            nombre = input("Nombre: ")
            usuario = Usuario(user_id, nombre)
            biblioteca.registrar_usuario(usuario)

        elif opcion == '4':
            user_id = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(user_id)

        elif opcion == '5':
            isbn = input("ISBN del libro a prestar: ")
            user_id = input("ID del usuario: ")
            biblioteca.prestar_libro(isbn, user_id)

        elif opcion == '6':
            isbn = input("ISBN del libro a devolver: ")
            user_id = input("ID del usuario: ")
            biblioteca.devolver_libro(isbn, user_id)

        elif opcion == '7':
            termino = input("Término de búsqueda: ")
            criterio = input("Criterio (titulo/autor/categoria): ")
            resultados = biblioteca.buscar_libros(termino, criterio)
            for libro in resultados:
                estado = "Prestado" if libro.prestado else "Disponible"
                print(f"- {libro.titulo} por {libro.autor} - {estado}")

        elif opcion == '8':
            user_id = input("ID del usuario: ")
            biblioteca.listar_libros_prestados(user_id)

        elif opcion == '9':
            biblioteca.mostrar_libros()

        elif opcion == '10':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()