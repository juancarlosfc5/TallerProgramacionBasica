'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que calcule el factorial de un número entero positivo
'''
print('Bienvenido al programa que calcula el factorial de un número entero positivo')
n = int(input('Introduzca un numero entero positivo: '))
factorial = int(1)
for i in range(1,n+1):
    factorial *= i
print(f'El factorial del número {n} es: {factorial}')