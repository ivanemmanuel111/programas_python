# Calcular la suma y el promedio de cuatro calificaciones

print('Calculando el promedio de cuatro calificaciones')
print('Dame 4 calificaciones separadas por un espacio:')
c1, c2, c3, c4 = input().split()
c1, c2, c3, c4 = [float(c1), float(c2), float(c3), float(c4)]
suma = c1 +c2 +c3 + c4
prom = suma / 4
print(f'La suma de : {c1}, {c2}, {c3}, {c4} es {suma} y el promedio es {prom}')

