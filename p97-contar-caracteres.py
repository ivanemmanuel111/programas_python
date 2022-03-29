#Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada
#carácter en la cadena.

cadena = input('Escribir la cadena a leer apariciones de caracteres:\n ')

diccionario = {}
#Diccionario guardara los caracteres de la cadena escrita
for c in cadena:
    diccionario[c] = diccionario.get(c, 0) + 1
#Entrega la lecttura de caracteres por la cadena
print(diccionario)
#Imprime el diccionario ya guardado con los caracteres mostrados y contados