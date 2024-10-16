'''
Fecha: 2024-09-15
Autor: Juan Carlos Flórez Cubides
Problema: Calcular el salario neto de un trabajador luego de aplicar los impuestos del país.
'''
print('Bienvenido al programa que permite calcular el salario neto de un trabajor luego de aplicar los impuestos correspondientes a su país')
paises = '1= País A\n2= País B\n3= País C\n4= Demás países'
salario_bruto = float(input('Ingrese su salario bruto: '))
print(paises)
salario_neto = "0"
pais = input('Ingrese el número correspondiente a su país: ')
match pais:
        case '1':
            salario_neto = round(float(salario_bruto*(1-0.2)),2)
            print(f'El salario neto aplicando los impuestos del 20% para el país A es {salario_neto}')
        case '2':
            salario_neto = round(float(salario_bruto*(1-0.15)),2)
            print(f'El salario neto aplicando los impuestos del 15% para el país B es {salario_neto}')
        case '3':
            salario_neto = round(float(salario_bruto*(1-0.1)),2)
            print(f'El salario neto aplicando los impuestos del 10% para el país C es {salario_neto}')
        case '4':
            salario_neto = round(float(salario_bruto*(1-0.25)),2)
            print(f'El salario neto aplicando los impuestos del 25% para los demás países es {salario_neto}')
        case _:
            print('Error en la opcion seleccionada')