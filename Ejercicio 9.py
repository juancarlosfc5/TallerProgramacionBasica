'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que clasifique a las personas de acuerdo a su rango de edad
'''
print('Bienvenido al programa que clasifica a las personas de acuerdo a su edad')
edad = int(input('Ingresa la edad de la persona que desea clasificar: '))
if (edad >= 0 and edad <= 12):
    print(f'La persona es un niño')
elif (edad >= 13 and edad <= 17):
    print(f'La persona es un adolescente')
elif (edad >= 18 and edad <= 64):
    print(f'La persona es un adulto')
elif (edad >= 65):
    print('La persona es un anciano')
else:
    print('El valor ingresado de edad es incorrecto')