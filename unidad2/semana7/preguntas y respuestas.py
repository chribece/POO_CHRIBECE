import time
#Clase principal
class PreguntasRespuestas:
#Metodo constructor
   def __init__(self):
#atributos
       self.preguntas = [ #Diccionario pregunta y respuesta
            {"pregunta": "¿Cuál es la capital de Ecuador?", "respuesta": "Quito"},
            {"pregunta": "¿Cuántos planetas hay en el sistema solar?", "respuesta": "8"},
            {"pregunta": "¿Cuánto es 10*5 ?", "respuesta": "50"}
        ]
       self.puntaje=0 #contador
       self.tiempo_inicio = time.time()# Registra el tiempo de inicio del juego
       print("¡Bienvenido al Juego de Preguntas y Respuestas!")
#Metodo especifico Jugar
   def jugar(self):
       for pregunta in self.preguntas:
           print(pregunta["pregunta"])
           respuesta=input("Tu respuesta: ")
           if respuesta.lower()==pregunta["respuesta"].lower():
               print("Respuesta correcta \n")
               self.puntaje+=1
           else:
               print(f"Incorrecto. La respuesta correcta es:{pregunta['respuesta']}")
       print(f"Puntaje final {self.puntaje}/{len(self.preguntas)}")
#Metodo destructor
   def __del__(self):
       tiempo_fin = time.time()
       tiempo_total = tiempo_fin - self.tiempo_inicio
       print("Fin del juego. ")
       print(f"Tiempo total: {tiempo_total:.2f} segundos.")
       print("¡Gracias por jugar!")


#Instancias
juego = PreguntasRespuestas()#llamada al constructor
juego.jugar()#ejecuta el juego