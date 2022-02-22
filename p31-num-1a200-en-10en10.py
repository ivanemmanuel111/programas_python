# numeros de 1 a 200 de 10 en 10

c = 1
n = int(input('Hasta donde ? '))
while c <= n:
    c += 1
    if c % 10 != 0: # todo aquel numero que residuo no me de 10 lo descarto
        continue
    print(c, end= ' ')