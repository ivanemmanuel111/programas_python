# Nombres y edades
#Diccionario con valorres introducidos por el usuario
# Diciionarios no permiten elementos repetidos
datos = {} #Diccionario vacio
print('Introduce nombres y edades * para termnar')

while True:
    nombre = input('Dame el nombre ? ')
    if nombre!='*': #Teclea * se rompe el ciclo
        edad = int(input('Edad ? '))
        datos[nombre]=edad #Entrada al diccionario
    else:
        break
print(f'El diccionario de datos creado: {datos}')