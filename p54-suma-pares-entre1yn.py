# Se desea imprimir los pares de 2 a n y su suma
# Ejemplo: Dame número ? 20 Salida: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 , La suma es = 189

n = int(input('Hasta que numero? '))
s=0
print('Salida: ')
for x in range(2, n,1): #(1 empieza, 101, hasta, 1 incremento)
    
    print(x,end=' ')
for i in range(2, n,1):   
    s += i
print(f'\nLa suma es: {s} ')