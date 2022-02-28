# Se desea imprimir los números impares de forma ascendente desde 1 hasta el número que el usuario decida (n)
# Además deberá imprimirse la suma de esos números impares. 



while(True): #While para preguntar y repetir el ciclo
    n = int(input('Hasta que numero? ')) #hace la pregunta para entrar
    c = 1 #tiene que estar en este ciclo al igual que s
    s = 0
    while c <= n: # ascendientes
        print(c, end= ' ') 
        s += c #suma el resultado
        c += 2 #para que sea impar
    print(f'La suma de los numero impares es {s}')
    if input('Deseas continuar (s/n)? ').upper()=='N' : break #pregunta nuevamente
print('......Gracias......')


