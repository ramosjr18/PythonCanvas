pregunta1 = input("Introduzca el primer numero: ")
pregunta2 = input("Introduzca el segundo numero: ")
operacion = input("Elija la operacion: +, -, *, / ")


def add():
    resultado = int(pregunta1) + int(pregunta2)
    return resultado


def sub():
    resultado = int(pregunta1) - int(pregunta2)
    return resultado


def mult():
    resultado = int(pregunta1) * int(pregunta2)
    return resultado


def div():
    resultado = int(pregunta1) / int(pregunta2)
    return float(resultado)

while True:
    if operacion == "+":    
        print(add())
        break
    elif operacion == "-":  
        print(sub())
        break
    elif operacion == "*":  
        print(mult())
        break
    elif operacion == "/":
        print(div())
        break
    else:
        print("Vuelve a Intentar ")
        operacion = ''
