# Calcula el factorial
# 5 factorial 1*2*3*4*5=120

n = int(input('Numero '))
f = 1
for i in range(1, n+1):
    f *= i
print(f'El factorial es {f}')