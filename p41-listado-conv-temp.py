# Se desea calcular la temperatura convertida de grados centígrados a grados farenheit 
# de un rango de valores introducidos por el usuario
# es decir el usuario introduce la temperatura inicial y la temperatura final en grados centígrados 
# y el programa realiza la conversión a farenheit incrementando el valor inicial en 1, hasta llegar al valor final.

while(True): #While para preguntar y repetir el ciclo
    
    g1 = float(input('Dame la temperatura inicial en celcius '))
    g2 = float(input('Dame la temperatura final en celcius '))

    f1 = int( (g1* 9/5) + 32 )
    f2 = int( (g2* 9/5) + 32 )
    print(f'Los grados iniciales farenheit son {f1} ')
    while f1 < f2:  
       
       print(f1, end= ' ') 
       f1 += 1
    print(f'Los grados farenheit finales son {f2}')
    if input('Deseas continuar (s/n)? ').upper()=='N' : break #pregunta nuevamente
print('......Gracias......')
