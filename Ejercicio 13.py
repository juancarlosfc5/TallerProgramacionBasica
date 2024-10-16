'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que compare tres números para determinar cual es el mayor
'''
print('Bienvenido al programa que determina cual es el número mayor entre 3 opciones')
numero1 = float(input('Ingrese el primer número: '))
numero2 = float(input('Ingrese el segundo número: '))
numero3 = float(input('Ingrese el tercer número: '))
if (numero1 > numero2 and numero1 > numero3):
    print(f'El número mayor es el número {numero1}')
elif (numero2 > numero1 and numero2 > numero3):
    print(f'El número mayor es el número {numero2}')
else:
    print(f'El número mayor es el número {numero3}')