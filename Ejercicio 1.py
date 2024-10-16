'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Establecer un programa que verifique si un número es par o impar
'''
print('Bienvenido al programa para verificar si un número es par o impar')
#Solicitar al usuario ingresar el número
numero = int(input('Ingrese el numero que desea verificar: '))
#Verificar si el número es par o impar
if (numero % 2 == 0):
    print(f'El número {numero} es par')
else:
    print(f'El número {numero} es impar')