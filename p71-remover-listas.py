# Remover elementos de una la lista

nums = [1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100]
print(f'Todos los números : {nums}')

nums.remove(99) #Buscar el elemento 99 y si existe lo elimina
print(f'Remover 99 : {nums}')

nums.pop(8) #Aqui va a la pos 8 y elimina el elemento que exista ahi
print(f'Remover [8] : {nums}')

nums.pop() #Remover el ultimo elemento de la lista
print(f'Remover el ultimo: 100 : {nums}')

nums.clear() #Eliminar todos los elementos de la lista
print(f'Remover todos : {nums}')