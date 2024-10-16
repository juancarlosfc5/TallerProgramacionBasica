'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Diseñar un programa que cuente las vocales en una cadena
'''
print('Bienvenido al programa que cuenta las vocales de una frase')
vocales = 'aeiouAEIOU'
mensaje = input('Escriba el mensaje para el cual quiere contar las vocales: ')
totalVocales=int(0)
for i in mensaje:
    if i in vocales:
        totalVocales +=1
print(f'Total de vocales encontradas en "{mensaje}" fueron : {totalVocales}')