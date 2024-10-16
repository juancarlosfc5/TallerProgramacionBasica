'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Establecer un programa que determine si el año es o no bisiesto
'''
print('Bienvenido al programa para verificar si el año es bisiesto')
año = int(input('Ingrese el año que desea verificar: '))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f'El año {año} es bisiesto')
else:
    print(f'El año {año} no es bisiesto')