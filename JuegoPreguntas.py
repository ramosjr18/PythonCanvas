#Juego de Preguntas

#variable para dar puntuacion al usuario
score = 0

#preguntas y verificacion de respuestas
pregunta1 = input("Cual es la capital de Panamá? ").lower()
if (pregunta1 == "panama" ):
    print("correcto")
    score +=  1
else:
    print("Incorrecto")

pregunta2 = input("En que continente queda Costa Rica? ").lower()
if (pregunta2 == "america" ):
    print("correcto")
    score +=  1
else:
    print("Incorrecto")

pregunta3 = input("En que pais esta Barcelona? ").lower()
if (pregunta3 == "españa" ):
    print("correcto")
    score +=  1
else:
    print("Incorrecto")

pregunta4 = input("En que continente se encuentra el Everest? ").lower()
if (pregunta4 == "asia" ):
    print("correcto")
    score +=  1
else:
    print("Incorrecto")

#le da el resultado al usuario
print("Haz obtenido", score, "puntos.")