import os
import subprocess
from pathlib import Path

# Configuración de colores para la terminal (opcional)
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def mostrar_codigo(ruta_script):
    """
    Muestra el contenido de un archivo Python.
    :param ruta_script: Ruta del archivo a leer.
    """
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            print(f"\n{Colors.OKBLUE}--- Código de {ruta_script} ---{Colors.ENDC}\n")
            print(archivo.read())
    except FileNotFoundError:
        print(f"{Colors.FAIL}El archivo no se encontró.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Ocurrió un error al leer el archivo: {e}{Colors.ENDC}")


def ejecutar_codigo(ruta_script):
    """
    Ejecuta un script Python en una nueva terminal.
    :param ruta_script: Ruta del script a ejecutar.
    """
    try:
        if os.name == 'nt':  # Windows
            subprocess.run(['python', ruta_script], shell=True)
        else:  # Unix-based systems
            subprocess.run(['gnome-terminal', '--', 'python3', ruta_script])
    except Exception as e:
        print(f"{Colors.FAIL}Ocurrió un error al ejecutar el código: {e}{Colors.ENDC}")


def mostrar_menu():
    """
    Muestra el menú principal y gestiona la navegación.
    """
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'UNIDAD1/SEMANA2/ejemplo cuenta bancaria.py',
        '2': 'UNIDAD1/SEMANA2/tecnicas de programacion.py',
        '3': 'UNIDAD1/SEMANA3/poo promedio semanal clima.py',
        '4': 'UNIDAD1/SEMANA3/programacion tradicional promedio semanal clima.py',
        '5': 'UNIDAD1/SEMANA4/EjemplosMundoReal_POO/Gestión de Inventario.py',
        '6': 'UNIDAD2/SEMANA5/analisis de datos.py',
        '7': 'UNIDAD2/SEMANA6/Sistema de Productos.py',
        '8': 'UNIDAD2/SEMANA7/preguntas y respuestas.py',
    }

    while True:
        print(f"\n{Colors.HEADER}******** Menu Principal - Dashboard *************{Colors.ENDC}")
        print(f"{Colors.BOLD}Selecciona un script para ver su código o ejecutarlo:{Colors.ENDC}")
        for key, value in opciones.items():
            print(f"{Colors.OKBLUE}{key} - {value}{Colors.ENDC}")
        print(f"{Colors.WARNING}0 - Salir{Colors.ENDC}")

        eleccion = input(f"{Colors.BOLD}Elige una opción: {Colors.ENDC}")
        if eleccion == '0':
            print(f"{Colors.OKGREEN}Saliendo del programa. ¡Hasta luego!{Colors.ENDC}")
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            if os.path.exists(ruta_script):
                mostrar_codigo(ruta_script)
                ejecutar = input(f"{Colors.BOLD}¿Deseas ejecutar este script? (1: Sí, 0: No): {Colors.ENDC}")
                if ejecutar == '1':
                    ejecutar_codigo(ruta_script)
                elif ejecutar == '0':
                    print(f"{Colors.WARNING}No se ejecutó el script.{Colors.ENDC}")
                else:
                    print(f"{Colors.FAIL}Opción no válida.{Colors.ENDC}")
            else:
                print(f"{Colors.FAIL}El archivo no existe en la ruta especificada.{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}Opción no válida. Por favor, intenta de nuevo.{Colors.ENDC}")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()