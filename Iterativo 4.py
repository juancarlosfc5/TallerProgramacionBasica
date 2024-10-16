'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que imprima todos los numeros pares en un rango incluyendo los limites
'''
print('Bienvenido al programa que imprime todos los numeros pares en un rango incluyendo sus limites')
inferior = int(input('Introduzca un numero entero positivo del limite inferior: '))
superior = int(input('Introduzca un numero entero positivo del limite superior: '))
for i in range(inferior,superior+1):
    if (i % 2 == 0):
        print(f'{i}')
print('Estos fueron los números pares dentro del rango especificado')