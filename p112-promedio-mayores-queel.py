#  Promedio y mayores que el promedio
"""
Documentar funcion
Calcula el promedio de elementos de una lista
recibe una lista y regresa un num entero
"""
def promedio(lista):
    s = 0
    for n in lista:
      s += n
    return s / len(lista)

def mayoresprom(lista, prom):
    mp = []
    for n in lista:
      if n > prom :
         mp.append(n)
    return mp

def leerdatos():
    datos=[]
    while True:
       d=float(input("número: "))
       if d==-1: break; #-1 ya no quiero introducir numero
       datos.append(d)
    return datos

# Programa principal
nums = leerdatos() #aqui yo meto los numeros
#nums = [9, 8, 7.5, 6, 9.5, 7, 10, 6, 7]
print(f'Los números son: {nums}')
prom = promedio(nums)
mp = mayoresprom(nums,prom)
print(f'El promedio es: {prom}')
print(f'Mayores al promedio es : {mp} - {len(mp)}')
