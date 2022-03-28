# Calificaciones

materias = ['Fisica', 'Quimica', 'Matematicas',
'Geografia', 'Estadistica']
califs = [10, 9, 8, 7.5, 6]
notas = dict(zip(materias, califs))
print(f'\nDiccionario nuevo : {notas}')

# actualizar diccionario para agregar elementos
notas.update({'Ingles':10})
notas.update({'Programacion':7})
print(f'\nDiccionario actualizado : {notas}')

# remover elementos del diccionario
notas.pop('Fisica')
notas.popitem()
print(f'\nDiccionario actualizado : {notas}')

# actualizar diccionario en elementos existentes
notas.update({'Quimica':10})
notas.update({'Matematicas':10})
print(f'\nDiccionario actualizado : {notas}')

# imprimir todo el diccionario elemento por elemento
print('\nTodos los elementos del diccionario')
for m,c in notas.items():
    print(f'{m:<12} - {c:5}')
# remover todos los elementos del diccionario
notas.clear()
print(f'\nDiccionario actualizado : {notas}')