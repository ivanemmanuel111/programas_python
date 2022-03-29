#Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada
#palabra en la cadena.

d = {} #Diccionario 
cadena = input("Cual es la cadena a leer?\n ")
print('')

lista_palabras=cadena.split(" ") #seperar las palabras
for palabra in lista_palabras:
	if palabra in d:
		d[palabra]+=1
	else:
		d[palabra]=1	

for campo,valor in d.items():
    print(f'{campo} Aparece en cantidad de {valor} veces')


