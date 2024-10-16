'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que calcule el costo del estacionamiento con tarifas progresivas
'''
print('Bienvenido al programa que calcula el costo del estacionamiento')
tiempo = int(input('Ingresa la cantidad de horas que estuvo en el estacionamiento: '))
costo = int(0)
if (tiempo <= 1):
    costo = 5
    print(f'El costo total del parqueadero por {tiempo} horas es de $5')
elif (tiempo > 1 and tiempo <= 4):
    costo = (tiempo-1)*4+5
    print(f'El costo total del parqueadero por {tiempo} horas es de ${costo}')
elif (tiempo > 4):
    costo = (tiempo-4)*3+17
    print(f'El costo total del parqueadero por {tiempo} horas es de ${costo}')
else:
    print('Incorrecto, recuerda que las horas deben ser positivas')