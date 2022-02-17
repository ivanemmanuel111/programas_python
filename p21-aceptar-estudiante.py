# Aceptar estudiantes mayores de edad con calificacion o igual a 8

print('Evaluando estudiantes mayores de edad con calificaciones mayores >= 8 ')
nombre = input('Dame tu nombre ?')
edad = int(input('Edad ?'))
if edad >= 18:
    print('Dame 2 calificaciones: ')
    c1, c2 = input().split()
    c1, c2 = [int(c1), int(c2)]
    if c1>=8 and c2>=8:
        print(f'{nombre} bienvenido, edad {edad}, calificaciones {c1},{c2}')
    else :
        print('solo aceptamos mayores a 8')
else :
    print('solo aceptamos mayores de edad')
