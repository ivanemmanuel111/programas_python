# Se desea calcular la suma y el promedio de una serie de números introducidos por el teclado
# Además deberá contar cuantos números se introdujeron, el proceso se detiene al introducir 0. 

while(True): #While para preguntar y repetir el ciclo
    c = 0
    s = 0
    num = 1
    while num != 0:  
        num = int(input('Escribir el numero a sumar: '))
        print('Al presionar 0 termina el contador de sumar')
        if num != 0:
           s += num
           c += 1

    if c == 0:
        print('No escribiste algun numero a sumar')
    else:
        prom = s / c

        print(f'El promedio de los {c} números es igual a {prom}')
    if input('Deseas continuar (s/n)? ').upper()=='N' : break
print('......Gracias......')   