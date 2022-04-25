#programa importante

import pandas as pd
datos = pd.read_csv('edades.csv',header = None, index_col = 0).squeeze(1)
datos.name = 'Edades'
print(datos)
#Acceder a los datos de una serie en base a su indice numerico

#Edad de carlos, elemento que esta en la posicion 0
print(datos[0])
#Los 3 primeros datos
print(datos[:3])
#Los 3 ultimos datos
print(datos[-3:])
#Elementos consecutivos
print(datos[6:11])
#Elementos no consecutivos
print(datos[[0,3,6]])