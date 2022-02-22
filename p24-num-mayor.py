# Realizar un programa que pida tres números y que diga cual es el mayor de los tres.

n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))
n3 = int(input('Ingrese el tercer numero: '))

if n2<n1>n3:
    print(f'El numero mayor es el primer que es {n1}')
elif n1<n2>n3:
    print(f'El numero mayor es el segundo que es {n2}')
elif n1<n3>n2: 
    print(f'El numero mayor es el tercer que es {n3}')
