# Se desea imprimir los números pares desde 100 hasta el número que el usuario decida (n)
# Además deberá imprimirse la suma de esos números pares. 


while(True): #While para preguntar y repetir el ciclo
    n = int(input('Hasta que numero? ')) #hace la pregunta para entrar al ciclo
    c = 100 #tiene que estar en este ciclo al igual que s
    s = 0
    while c >= n: #descendientes
        print(c, end= ' ') 
        s += c #suma el resultado
        c -= 2 #para que sea par
    print(f'La suma de los numero impares es {s}')
    if input('Deseas continuar (s/n)? ').upper()=='N' : break
print('......Gracias......')