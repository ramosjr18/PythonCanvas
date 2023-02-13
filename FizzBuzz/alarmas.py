# Objetivo es Crear un sistema de alertas con el algoritmo fizzbuzz
# en el que se trabaja un tema distinto cada 3-4 horas 

list = [3,4,5,6,7,8,9,10,11,12,13,14,15]

def alertas():
    for i in list:
        if i % 3 == 0:
            print('')
            print('Una alarma aqui \nEmpieza un tema nuevo')
            print('')
        elif i % 5 == 0: 
            print('un break aqui')
            print('')
        else:
            print('No pasa nada')
            print('')


alertas()