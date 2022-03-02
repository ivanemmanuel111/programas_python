#Se desea imprimir la secuencia de números mostrados el numero de renglones que el usuario desee:
#Ejemplo: Dame número ? 4
#Salida:
#1
#1 2
#1 2 3
#1 2 3 4

r = int(input('Dame numero? '))
print('Salida: ')
for y in range(1, r+1):
    for x in range(1, y+1): #y+1 permite que inicie el triangulo en 1 y luego sea 12. 123
        print(x, end=' ') #print x muestra los numeros hasta el que digamos   
    print('') 