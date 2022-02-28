# Calcular el número mayor de una serie de números introducidos por el teclado
# El proceso se detiene al introducir 0.

while(True): #While para preguntar y repetir el ciclo
    x = 0
    n = 0
    c = 0
    mayor = 0
    n = int (input('Cuantos numeros '))
    while c<=n-1:
        c+=1
        x=int(input('Ingrese numero '))
        if c==1:
            mayor=x
        elif x>mayor:
            mayor=x
    print(f'El numero mayor es: {mayor}')
    
    if input('Deseas continuar (s/n)? ').upper()=='N' : break
print('......Gracias......')   