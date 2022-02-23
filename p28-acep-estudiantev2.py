# La Universidad Kitty Kat SA es solo para mujeres mayores de 21 años con un promedio de entre 8 y 9.5. 
# Elabore un programa que pida el Nombre de la estudiante, su edad, tres calificaciones 
# decida si la estudiante es aceptada

print('Evaluando estudiantes mujeres mayores de 21 años de edad con calificaciones mayores >= 8 ')
nombre = input('Dame tu nombre ')
edad = int(input('Edad? '))
if edad >= 21:
    print('Dame 3 calificaciones: ')
    c1, c2, c3 = input().split()
    c1, c2, c3 = [float(c1), float(c2), float(c3)]
    prom = (c1 + c2 +c3) / 3
    if prom>=8 and prom<=9.5:
        print(f'{nombre} bienvenida, edad {edad}, promedio de {prom}')
    else :
        print('solo aceptamos con promedio entre 8 y 9.5')
else :
    print('solo aceptamos mayores de 21 años de edad')
