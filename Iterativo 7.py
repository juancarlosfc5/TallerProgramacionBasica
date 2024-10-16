'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que sume numeros pares hasta que se digite un numero impar
'''
print('Bienvenido al programa que suma números pares')
suma = int(0)
numero = int(0)
while numero % 2 == 0:
    numero = int(input('Ingrese el numero par que desea sumar\nPara salir del programa ingrese un múmero impar: '))
    if (numero % 2 == 0):
        suma += numero
print(f'La suma de los números pares ingresado es {suma}')