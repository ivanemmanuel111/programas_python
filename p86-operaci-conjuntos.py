#Operaciones sobre conjuntos
import os
os.system('cls')

print("Conjuntos y operaciones sobre ellos :")
municipios = {"Zacatecas", "Guadalupe","Jerez","Fresnillo", "Fresnillo"}

print(f"El conjunto original : {municipios}")
print(f"\nLa colección es del tipo : {type(municipios)}") #Muestra que si es conjunto
print(f"Longitud del conjunto : {len(municipios)}")

print("\nLista de municipios usando un ciclo: ")
for c in municipios: #Imprimir los conjuntos
     print(c) 

print(f"\nEsta Zacatecas en el conjunto: {'Zacatecas' in municipios}")
print("\nAgregra elementos a un conjunto:")
municipios.add("Teul") #Agregar municipio

print(f"Agregar con Add : {municipios}")
otrosmunicipios = {"Luis Moya","Ojocaliente","Tepetongo"}
municipios.update(otrosmunicipios)
print(f"Agregrar con Update : {municipios}") #Agregar conjunto

print("\nEliminar elementos del conjunto:")
municipios.remove("Zacatecas") # eliminar zacatecas
print(f"Municipios : {municipios}")

municipios.discard("Ojocaliente") # si no esta no hace nada
print(f"Municipios : {municipios}")

m = municipios.pop() # elimina el tope = el primero
print(m) #para observar cual borro al azar
print(f"Municipios : {municipios}")

municipios.clear() #eliminar todos
print(f"Municipios : {municipios}")
