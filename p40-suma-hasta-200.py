# Se desea calcular la suma de números introducidos por el usuario hasta que la sume llegue a 200
# Luego mostrar cuantos números fueron introducidos y la suma de estos

while(True): #While para preguntar y repetir el ciclo
    s = 0
    c = 0
    while s < 200:  
       n = int(input('Escribir el numero a sumar: '))
       s = s + n
       c = c + 1
    print(f'La suma de los numeros es {s} y entraron {c} numeros a sumar')
    if input('Deseas continuar (s/n)? ').upper()=='N' : break #pregunta nuevamente
print('......Gracias......')
