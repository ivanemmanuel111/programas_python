# Acceder a los elementos de una lista

nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]

print(f'Todos los números : {nums}')

print(f'Cuantos elementos son : {len(nums)}')
print(f'Primero y último : {nums[0]}, {nums[-1]}')
print(f'Del 2 al 6 : {nums[2:6]}')
print(f'Los primeros 3 : {nums[:3]}')
print(f'Los últimos 3 : {nums[6:]}')
print(f'3 antes del último : {nums[-4:-1]}')