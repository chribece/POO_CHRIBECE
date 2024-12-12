
#definimos funcion para el ingreso de temperaturas
def ingresotemp():
    temperaturas=[]#almacenamos las temperaturas en una lista
    for dia in range(7):#dias de la semana
        temp=float(input(f"Ingresa la temperatura del dia{dia+1}:"))
        temperaturas.append(temp)
    return temperaturas
#definimos funcion para calcular el promedio
def calcpromsem(temperaturas):
    total=sum(temperaturas)#suma todas las temperaturas ingresadas
    promedio=total/len(temperaturas)#calcula el promedio para el numero de dias
    return promedio
#llamada a las funciones
def main():
    temperaturas=ingresotemp()
    promedio=calcpromsem(temperaturas)
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}°c")

if __name__=="__main__":
    main()
