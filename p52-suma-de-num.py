# suma de numeros introducidos por el usuario

n = int(input('Cuantas calificaciones? '))
s = 0
for i in range(1, n+1): #no puede con float
    c = float(input(f'Calificacion {i}? '))
    s += c
print(f'La suma es {s} y el promedio es {s/n}')
