# Dado un numero entero entre 1 y 7, se desea mostrar con letra el día de la semana correspondiente, 1 es domingo, 2 es lunes y así hasta 7 es viernes.
# Si el número no está especificado, mostrar un mensaje que diga “Día incorrecto”.

num = int(input('Ingresa un numero: '))

if num == 1:
    print('Domingo')
elif num == 2:
    print('Lunes')
elif num == 3:
    print('Martes')
elif num == 4:
    print('Miercoles')
elif num == 5:
    print('Jueves')
elif num == 6:
    print('Viernes')
elif num == 7:
    print('Sabado')
else:
    print('Dia incorrecto')
