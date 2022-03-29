# cuadro de r x c de un carácter

def cuadro_caracter(r, c, car): #3 parametros, renglones, columnas y que caracter
   for i in range(1, r+1): #renglones
      for j in range(1, c+1): #columnas
           print(car, end=' ') #caracter
      print('\r') #se salte una linea
r = int(input('Cuantos renglones? '))
c = int(input('Cuantas columnas? '))
car = input('Cual catacter? ')
cuadro_caracter(r, c, car) #mandar llamar la funcion

cuadro_caracter(4, 4, '$') #llamamos la funcion con otros valores

