'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Conversión de temperatura de grados Celcius a Fahrenheit
'''
print('Bienvenido al programa para convertir temperatura de grados Celcius a Fahrenheit y viceversa')
escala = '1= Celcius a Fahrenheit\n2= Fahrenheit a Celcius'
print(escala)
escala = input('Escoja la conversión que desea realizar: ')
Celsius = float(0)
Fahrenheit = float(0)
match escala:
    case '1':
        Celsius = float(input('Digite el valor de la temperatura en grados Celsius: '))
        Fahrenheit = round((Celsius*(9/5))+32,2)
        print(f'La temperatura convertida en grados Fahrenheit es {Fahrenheit}°F')
    case '2':
        Fahrenheit = float(input('Digite el valor de la temperatura en grados Fahrenheit: '))
        Celsius = round((Fahrenheit-32)*(5/9),2)
        print(f'La temperatura convertida en grados Celsius es {Celsius}°C')
    case _:
        print('Error en la opcion seleccionada')