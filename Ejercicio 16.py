'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que calcule el tiempo que demora en llegar un automovil a su destino
'''
print('Bienvenido al programa que calcula el tiempo de tu viaje')
distancia = float(input('Ingrese la distancia en Kilometros (Km): '))
velocidad = float(input('Ingrese la velocidad en Kilometros por hora (Km/h): '))
tiempo = '0'
tiempo = round(distancia/velocidad,1)
if (distancia < 0):
    print('Recuerda que las distancias no son negativas')
elif (velocidad > 0 and velocidad < 120):
    print(f'El tiempo de tu viaje será {tiempo} horas')
elif (velocidad >= 120):
    print(f'El tiempo de tu viaje será {tiempo} horas, sin embargo, ten cuidado vas a una velocidad muy alta!!!')
else:
    print('Ingresaste un valor erroneo de velocidad')