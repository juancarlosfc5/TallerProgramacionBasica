'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que asigne una calificación de notas basadas en una nota númerica
'''
print('Bienvenido al programa que asigna una calificación basado en una nota númerica de una escala de 0 a 100')
nota = float(input('Ingresa la nota númerica de la persona para asignar la calificación: '))
if (nota >= 90 and nota <= 100):
    print('La persona obtuvo una calificación A')
elif (nota >= 80 and nota <= 89):
    print('La persona obtuvo una calificación B')
elif (nota >= 70 and nota <= 79):
    print('La persona obtuvo una calificación C')
elif (nota >= 60 and nota <= 69):
    print('La persona obtuvo una calificación D')
elif (nota >= 0 and nota < 60):
    print('La persona obtuvo una calificación F')
else:
    print('El valor ingresado de nota númerica es incorrecto, recuerda que la escala es de 0 a 100')