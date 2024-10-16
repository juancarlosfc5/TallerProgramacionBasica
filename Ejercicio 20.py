'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que convierta una calificación númerica en una calificación en letras
'''
print('Bienvenido al programa que convierte una calificación númerica en una calificación en letras')
nota = float(input('Ingresa la nota númerica entre 0 y 100 de la persona para asignar la calificación: '))
match nota:
    case nota if (nota >= 90 and nota <= 100):
        print('La persona obtuvo una calificación A')
    case nota if (nota >= 80 and nota < 90):
        print('La persona obtuvo una calificación B')
    case nota if (nota >= 70 and nota < 80):
        print('La persona obtuvo una calificación C')
    case nota if (nota >= 60 and nota < 70):
        print('La persona obtuvo una calificación D')
    case nota if (nota >= 0 and nota < 60):
        print('La persona obtuvo una calificación F')
    case _:
        print('El valor ingresado de nota númerica es incorrecto, recuerda que la escala es de 0 a 100')