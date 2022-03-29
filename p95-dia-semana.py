#Cree un diccionario con los días de la semana: la llave es el número de día y el valor es el día con letra
# 1,2,3,4,5,6,7
# Lunes, Martes, Miércoles, Jueves, Viernes
#Luego se le pide al usuario un número de día y se imprime su correspondiente con letra, usando los valores
#previamente almacenados en el diccionario.

semana = {1: 'Lunes', 2: 'Martes', 3: 'Miercoles', 4:'Jueves', 5: 'Viernes', 6: 'Sabado', 7:'Domingo'}
d = semana[int(input('Dame el numero de dia de la semana '))]

print(f'El dia es {d}')
