#Se desea imprimir la secuencia de números mostrados el numero de renglones que el usuario desee:
#Ejemplo: Dame número ? 4
#Salida:
#1
#2 2
#3 3 3
#4 4 4 4

r = int(input('Dame numero? '))
print('Salida: ')
for x in range(1, r+1):
    for y in range(1, x+1):
        print(x, end=' ') #print x muestra los numeros hasta el que digamos
    print('')