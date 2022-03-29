# Tabla de multiplicar

def tabla_multiplicar(t, n):
   for i in range(1, n+1):
      print(f'{t} x {i} = {t * i}') #El for es para realizar la multiplicacion
   print('\n') #espacio entre cada tabla
t = int(input('Que tabla quieres? '))
n = int(input('Hasta donde? '))
tabla_multiplicar(t, n)

tabla_multiplicar(4, 10) #mandar llamar la funcion con otros datos
