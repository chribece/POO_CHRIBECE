# El siguiente programa calcula la media, mediana y moda de una lista
# Incluye diferentes tipos de datos, como listas para almacenar los números y flotantes para calcular la media.
# El código utiliza identificadores descriptivos siguiendo la convención snake_case
# Contiene comentarios relevantes que explican la lógica utilizada

#funcion para calcular la media
def calcula_media(numeros):
    return sum(numeros)/len(numeros)

#funcion para calcular la mediana

def calcula_mediana(numeros):
    numeros.sort() #ordenamos la lista
    longitud=len(numeros)#obtenemos la longitud
    if longitud%2==0:#validamos si la cantidad de números es par
        return (numeros[longitud//2-1]+numeros[longitud//2])/2
    else:#caso contrario la cantidad de números es impar
        return numeros[longitud//2]

#funcion para calcular la moda

def calcula_moda(numeros):
    from collections import Counter #Importamos Counter para contar las veces que se repite un número
    contador=Counter(numeros)#cantidad de veces que se repite cada número
    max_repeticiones=max(contador.values())
    return [numero for numero, frecuencia in contador.items() if frecuencia==max_repeticiones]

#Lista de numeros para el analisis de datos
numeros = [4, 5.5, 6, 4, 7, 8, 4, 5, 7.5, 6] #[1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5]

#Impresión de resultados
print("Media:", calcula_media(numeros))
print("Mediana:", calcula_mediana(numeros))
print("Moda:", calcula_moda(numeros))
