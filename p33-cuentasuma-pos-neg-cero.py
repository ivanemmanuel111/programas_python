# Cuenta y suma, positivos, negativos, ceros
c=s=cp=cn=cc = 0
while True:
    n = int(input('Numero? '))
    if n == 999: break
    s += n
    c += 1
    if n>0 : cp+=1
    elif n<0 : cn+=1
    else: cc+=1
    
print(f'Se introdujeron {c}')
print(f'Pos: {cp}, Neg: {cn}, ceros: {cc}')
print(f'La suma de los numero es {s}')
