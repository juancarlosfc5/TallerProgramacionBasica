'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Adivinar la letra secreta
'''
print('Bienvenido al programa para adivinar una letra secreta')
secreta = "A"
letra = input('Escribe la letra que consideras es la letra secreta:\n Recuerda escribir la letra mayuscula ')
match letra:
    case "A":
        print('Felicidades adivinaste la letra!!!!, reclama el premio en la cafetería')
    case _:
        print('Lo siento, sigue intentando adivinar la letra secreta')