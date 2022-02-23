# Realizar un programa que pida tres números consecutivos (3,4,5 o 9,10,11)
# Si no son consecutivos que mande un mensaje de error
# cuando sean consecutivos que diga “gracias” y termine el programa.

n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))
n3 = int(input('Ingrese el tercer numero: '))

if n2 == n1 + 1 and n3 == n2 + 1:
    print('Gracias')
else:
    print('error')

