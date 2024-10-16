'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Imprimir el dia correspondiente de la semana usando los numeros del 1 al 7
'''
print('Bienvenido al programa que imprime el día correspondiente de la semana usando los numeros de cada dia')
DiasSemana = '1= Lunes\n2= Martes\n3= Miércoles\n4= Jueves\n5= Viernes\n6= Sábado\n7= Domingo'
print(DiasSemana)
numero = int(input('Ingrese un número del 1 al 7: '))
match numero:
        case '1':
            print('El día de la semana es Lunes')
        case '2':
            print('El día de la semana es Martes')
        case '3':
            print('El día de la semana es Miércoles')
        case '4':
            print('El día de la semana es Jueves')
        case '5':
            print('El día de la semana es Viernes')
        case '6':
            print('El día de la semana es Sábado')
        case '7':
            print('El día de la semana es Domingo')
        case _:
            print('Error en la opcion seleccionada')