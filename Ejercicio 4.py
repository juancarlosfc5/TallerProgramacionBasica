'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que indique el tipo de triangulo en funcion de sus lados
'''
print('Bienvenido al programa que indica el tipo de triangulo en funcion de la longitud de sus lados')
numero1 = float(input('Introduzca la longitud del primer lado del triangulo: '))
numero2 = float(input('Introduzca la longitud del segundo lado del triangulo: '))
numero3 = float(input('Introduzca la longitud del tercer lado del triangulo: '))
if (numero1 == numero2 and numero2 == numero3):
    print('El triangulo es equilatero')
elif (numero1 == numero2 or numero2 == numero3 or numero1 == numero3):
    print('El triangulo es isóceles')
else:
    print('El triangulo es escaleno')