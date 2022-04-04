#Diseña un programa con una función que pida un número entero entre 1 y 7 y devuelva el día de la semana con
#letra (ver p101 - estación del año).

def dia(n):
  if n==1:
     est='Lunes'
  elif n==2:
     est='Martes'
  elif n==3:
     est='Miercoles'
  elif n==4:
     est='Jueves'
  elif n==5:
     est='Viernes'
  elif n==6:
     est='Sabado'
  elif n==7:
     est='Domingo'  
  else:
     est='Error'
  return est

n = int(input('Dame el dia de la semana (1-7)? '))
e = dia(n)
if dia(n) == 'Error':
    print(f'Dia no listado')
else:
    print(f'El dia de la semana es: {e}')