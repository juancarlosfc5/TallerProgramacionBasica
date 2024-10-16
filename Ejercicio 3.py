'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Crear una calculadora que realice las operaciones basicas para 2 numeros
'''
import os
isActive = True
opcionesCalculadora = '+. Suma\n-. Resta\n*. Multiplicacion\n/. Division\n0. Salir'
opcionesUsuario = ''
resultado = 0
while (isActive):
    print('Bienvenido a la calculadora simple para 2 numeros')
    numero1 = float(input('Introduzca el primer numero que desea operar: '))
    numero2 = float(input('Introduzca el segundo numero que desea operar: '))
    print(opcionesCalculadora)
    opcionesUsuario = input(':_')
    match opcionesUsuario:
        case '+':
            resultado = numero1 + numero2
            print(f'El resultado de la suma de {numero1} y {numero2} es {resultado}\n ')
        case '-':
            resultado = numero1 - numero2
            print(f'El resultado de la resta de {numero1} y {numero2} es {resultado}\n ')
        case '*':
            resultado = numero1 * numero2
            print(f'El resultado de la multiplicacion de {numero1} y {numero2} es {resultado}\n ')
        case '/':
            resultado = numero1 / numero2
            print(f'El resultado de la division de {numero1} y {numero2} es {resultado}\n ')
        case '0':
            isActive = False
        case _:
            print('Error en la opcion seleccionada')
            os.system('pause')