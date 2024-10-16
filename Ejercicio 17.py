'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que añada un sistema de bonificaciones a las calificaciones de un estudiante
'''
print('Bienvenido al programa que calcula la nota final teniendo en cuenta las bonificaciones')
NotaInicial = float(input('Ingrese su calificación inicial de una escala de 0 a 100: '))
bonificacion = '1= Si\n2= No'
print(bonificacion)
bonificacion = input('Cuenta con bonificación: ')
NotaFinal = '0'
match bonificacion:
        case '1':
            NotaFinal = round(float(NotaInicial*(1+0.05)),2)
            if (NotaFinal > 100):
                print('Su calificación final es 100')
            else:
                print(f'Su calificación final es {NotaFinal}')
        case '2':
            print(f'Su calificación final es {NotaInicial}')
        case _:
            print('Error en la opcion seleccionada')
