# Estudiantes

estudiante = {
'nombre':'Ivan',
'edad':24,
'email':'ivanemmanuel111@gmail.com',
'carrera':'Ing y Tec aplicada'
}

print(f'\nEl diccionario: {estudiante}')
print('\nLas llaves: ')
for k in estudiante.keys():
    print(k)

print('\nLos valores: ')
for v in estudiante.values():
    print(v)

print("\nLlaves y valores:")
for k,v in estudiante.items():
    print(f'{k:<10} : {v}') #En que posicion imprimir 
estudiante['calificacion']=9.5

print(f'\nEl diccionario actualizado: {estudiante}')