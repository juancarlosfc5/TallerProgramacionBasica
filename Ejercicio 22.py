'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que clasifique el tipo de triangulo en funcion de sus angulos
'''
print('Bienvenido al programa que indica el tipo de triangulo en funcion de sus angulos')
angulo1 = float(input('Introduzca el primer angulo en grados (°): '))
angulo2 = float(input('Introduzca el primer angulo en grados (°): '))
angulo3 = float(input('Introduzca el primer angulo en grados (°): '))
validacion = angulo1 + angulo2 + angulo3
if (validacion != 180):
    print('El triangulo no cumple la regla que indica que la suma de sus angulos debe ser igual a 180°')
elif (angulo1 == 90 or angulo2 == 90 or angulo3 == 90):
    print('El triangulo es recto')
elif (angulo1 > 90 or angulo2 > 90 or angulo3 > 90):
    print('El triangulo es obtuso')
elif (angulo1 < 90 and angulo2 < 90 and angulo3 < 90):
    print('El triangulo es agudo')
else:
    print('El triangulo no es valido')