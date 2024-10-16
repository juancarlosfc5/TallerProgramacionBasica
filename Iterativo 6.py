'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que genere un numero aleatorio entre 1 y 100 con el fin de crear un juego de adivianzas
'''
print('Bienvenido al juego de adivinanza de números entre 1 y 100')
import random
aleatorio = random.randint(1,100)
numero = float(0)
while numero != aleatorio:
    numero = int(input('Intenta adivinar el número aleatorio eligiendo un numero entre 1 y 100: '))
    if (numero == aleatorio):
        print(f'Felicidades adivinaste el número!!!! era {aleatorio}, reclama el premio en la cafetería')
    elif (numero < aleatorio):
        print(f'Lo siento el número que elegiste {numero} es menor que el numero secreto intenta nuevamente')
    else:
        print(f'Lo siento el número que elegiste {numero} es mayor que el numero secreto intenta nuevamente')