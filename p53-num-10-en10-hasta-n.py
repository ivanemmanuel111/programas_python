# Se desea imprimir los números de 1 a n de 10 en 10
# Ejemplo: Dame número ? 100 Salida. 1 11 21 31 41 51 61 71 81 91 

n = int(input('Dane hasta donde? '))
print('Salida: ')
for x in range(1, n+1,10): #(1 empieza, 101, hasta, 1 incremento)
    print(x,end=' ')