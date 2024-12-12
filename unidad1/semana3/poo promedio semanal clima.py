
# definimos clase1 contiene datos diarios del clima
class climaxdia:
    def __init__(self, temperatura): #inicializamos atributo
        self.temperatura = temperatura

# definimos clase2 contiene datos diarios del clima
class climaxsemana:
    def __init__(self):
        self.temperaturas = []#lista para almacenar las temperaturas diarias

    #metodo para agregar temperatura
    def adtemp(self, temperatura):
        self.temperaturas.append(climaxdia(temperatura))

    # metodo para calcular el promedio de las temperaturas
    def calcprom(self):
        total=sum([dia.temperatura for dia in self.temperaturas])
        promedio=total/len(self.temperaturas)
        return promedio

#Llamada de las funciones
def main():
    climasemana=climaxsemana()
    for dia in range(7):
        temp=float(input(f"Ingresa la temperatura del dia {dia+1}: "))
        climasemana.adtemp(temp)
    promedio=climasemana.calcprom()
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
