# Iterar sobre los elementos de la lista

nums = [2, 4, 6, 8, 10, 12, 14, 16]
print(f'Todos los números : {nums}')

print('\nIterar con ciclo for : ')
for n in nums: #En cada elemento de la lista hara algo
    print(f'{n:<15} - {n**2:<15} - {n**3:<15}') #que cada elemento se imprima

print('\nIterar con ciclo range : ', end='')
#Range
for i in range(len(nums)):
    print(f'{nums[i]} - {nums[i]+10}')

print(f'\nIterar con comprension : ', end='')
[print(n, end='/') for n in nums]

