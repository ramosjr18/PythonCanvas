#Juego de Preguntas

score = 0

pregunta1 = input("Cual es la capital de Panamá?").lower()
if (pregunta1 == "panama" ):
    print("correcto")
    score +=  1
else:
    print("Incorrecto")

pregunta2 = input("a?").lower()
if (pregunta2 == "a" ):
    print("correcto")
    score +=  1
else:
    print("Incorrecto")

pregunta3 = input("b?").lower()
if (pregunta3 == "b" ):
    print("correcto")
    score +=  1
else:
    print("Incorrecto")

pregunta4 = input("c?").lower()
if (pregunta4 == "c" ):
    print("correcto")
    score +=  1
else:
    print("Incorrecto")

print("Haz resuelto", score, "preguntas correctamente")
