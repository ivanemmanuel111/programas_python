# numero del 1 al 200 break 100
# 1 + 2 + 3 + 4 >= 100 
# Ejemplo con break

c = 0
s = 0
while c < 200:
    c += 1
    s += c
    print(c, end= ' ')
    if s >= 1000:
        print('\n')
        break      # uso del break
print(f'Hemos alcanzado la suma {s}')
