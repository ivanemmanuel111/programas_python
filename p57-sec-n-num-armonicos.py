#Se desea imprimir la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma:
#Ejemplo: Dame términos ? 5
#Salida: 1+1/2+1/3+1/4+1/5 , suma 2.283333333333333

n = int(input('Dame terminos: '))
a = 0
r = 0

for x in range(1, n+1,1): #(1 empieza, 101, hasta, 1 incremento)
    r = (1/x)
    
    print(r,end='+')
    a += r
    
print(f', Suma {a}')