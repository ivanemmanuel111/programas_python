#Calculando el area de un triangulo

#Entada
print('Calculando el area de un triangulo ...')
print('Dame la base y la altura del triangulo')
base, altura = int(input()), int(input()) # se leen dos datos a la vez separados por Enter
#Proceso
area = base * altura / 2
#Salida
print(f'Para un triangulo de base {base} y altura {altura} el area es {area}')
