#Se desea imprimir la secuencia de términos, el numero de renglones que el usuario desee y su suma:
#Ejemplo: Cuantos términos ? 5
#1+11+111+1111+11111
#suma 12345
r = int(input('Dame terminos: '))
n = 1
for x in range(1, r+1):
    print(n, end='+')
    
    for y in range(1, x+1):
        
        print(n, end='') #print x muestra los numeros hasta el que digamos
        
print('')
print('Suma')
for z in range(1, r+1,1): #(1 empieza, 101, hasta, 1 incremento)   
    print(z,end='')
    