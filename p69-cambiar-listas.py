
# Cambiar los elementos de una lista

nums = [10, 9, 8.5, 6.5, 9.8, 7, 5, 6.2, 9.5]

print(f'Todos los números : {nums}')

nums[0]=7 ; nums[1]=7 #Sustituir el primer elemento y el segundo por [7]
print(f'Poner en posicion 0 y 1 en 7 y 7 : {nums}')

nums[2:5] = [9,9,9] #Desde pos 2 a la 4, poner 9 en c/u
print(f'Desde 2:5 poner 9,9,9 : {nums}')

nums[5:1] = [10,10,10] #Desde la pos 5 a la 1, poner tres 10, por lo tanto recorre las demas posiciones
print(f'Desde 5:1 poner 10,10,10 : {nums}')

nums[8:12] = [8] #De la 8 a la 12 poner 8, rango suficiente pero menos valores
print(f'Poner de 8:12 el numero 8 : {nums}')