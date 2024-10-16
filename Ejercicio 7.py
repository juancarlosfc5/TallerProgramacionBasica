'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que indique si el número ingresado es positivo, negativo o cero
'''
print('Bienvenido al programa que indica si el número ingresado es positivo, negativo o cero')
numero = float(input('Ingresa el número que deseas verificar: '))
if (numero > 0):
    print(f'El número {numero} es positivo')
elif (numero < 0):
    print(f'El número {numero} es negativo')
else:
    print('El número ingresado es cero')