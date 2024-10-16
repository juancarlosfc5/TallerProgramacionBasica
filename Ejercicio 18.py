'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un sistema de evaluacion de creditos universitarios
que otorge la cantidad total de acuerdo a la aprobación de las materias
'''
print('Bienvenido al programa que calcula el número total de creditos del estudiante')
materias = int(input('Ingrese el numero de materias cursadas: '))
creditos = int(0)
for i in range(materias):
    nota = float(input(f'Ingrese la calificación obtenida en la materia {i+1}, en una escala de 0 a 100: '))
    if (nota >= 60):
        creditos += 3
        print(f'La materia {i+1} fue aprobada')
    else:
        print(f'La materia {i+1} fue reprobada')
print(f'El total de creditos aprobados por el estudiante para {materias} materias es de {creditos} creditos')