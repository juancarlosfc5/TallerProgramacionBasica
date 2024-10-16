'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que indique si el estudiante aprueba la materia respecto a la nota numerica
'''
print('Bienvenido al programa para verificar si el estudiante aprueba la materia respecto a la nota númerica')
#Solicitar al usuario ingresar la nota
nota = float(input('Introduzca la nota que obtuvo el estudiante, recuerde que debe ser un número entre 0 y 100: '))
#Verificar si con la nota el estudiante aprueba o no
if (nota >= 60 and nota <= 100):
    print(f'El estudiante con nota {nota} es aprobado')
elif (nota >= 0 and nota < 60):
    print(f'El estudiante con nota {nota} es reprobado')
else:
    print('No ingreso un valor valido')