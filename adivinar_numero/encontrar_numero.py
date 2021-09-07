import random

intentosRealizados = 0

print('Hola! Cuál es tu nombre?')
miNombre = input()

numero = random.randint(1, 20)
print('Bueno, ' + miNombre + ', estoy pensando en un numero entre 1 y 20.')

while intentosRealizados < 6:
    print('Intenta adivinar.')
    estimacion = input()
    estimacion = int(estimacion)

    intentosRealizados = intentosRealizados + 1

    if estimacion < numero:
        print('Tu estimacion es baja.')
    if estimacion > numero:
        print('Tu estimacion es alta.')
    if estimacion == numero:
        break

if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('Buen trabajo, ' + miNombre + 'Has adivinado el numero es ' + intentosRealizados + ' intentos!!!')

if estimacion != numero:
    numero = str(numero)
    print('Pues no. El numero que estaba pensando yo era ' + numero)