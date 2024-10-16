'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que calcule la suma de los primeros n numeros enteros
'''
print('Bienvenido al programa que calcula la suma de los primeros n numeros enteros')
n = int(input('Introduzca un numero entero positivo: '))
suma = int(0)
for i in range(1,n+1):
    suma += i
print(f'La suma de los primeros {n} numeros enteros es: {suma}')