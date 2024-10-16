'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que calcule el indice de masa corporal y entregue la clasificacion de estado de peso
'''
print('Bienvenido al programa que calcula el Indice de Masa Corporal (IMC) y entrega la clasificación de estado de peso')
peso = float(input('Ingrese su peso en Kilogramos (Kg): '))
altura = float(input('Ingrese su altura en Metros (m): '))
IMC = round((peso/(altura**2)),2)
if (IMC < 18.5):
    print(f'Su indice de masa corporal es {IMC} y su estado de peso es "Bajo peso"')
elif (IMC >= 18.5 and IMC < 25):
    print(f'Su indice de masa corporal es {IMC} y su estado de peso es "Peso normal"')
elif (IMC >= 25 and IMC < 30):
    print(f'Su indice de masa corporal es {IMC} y su estado de peso es "Sobrepeso"')
else:
    print(f'Su indice de masa corporal es {IMC} y su estado de peso es "Obesidad"')