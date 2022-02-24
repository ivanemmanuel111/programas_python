# suma de impares y sumas de pares hasta donde el usuario decida

n = int(input('Hasta donde? '))
s=0
print('\nnumeros impares')
for i in range(1, n+1,2):
    print(i,end=' ')
    s += i
print(f'\nsuma de impares: {s} ')

s=0
print('\nnumeros pares')
for i in range(2, n+1,2):
    print(i,end=' ')
    s += i
print(f'\nsuma de pares: {s} ')