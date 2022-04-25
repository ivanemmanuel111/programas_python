#programa importante

import pandas as pd
datos = pd.read_csv('edades.csv',header = None, index_col = 0).squeeze(1)
datos.name = 'Edades'
print(datos)
#Acceder a los datos de una serie en base a su indice numerico

#Edad de carlos, elemento que esta en la posicion 0
print(datos['Santiago'])
#Los 3 primeros datos
print(datos[:'Antonio'])
#Los 3 ultimos datos
print(datos['Claudia':])
#Elementos consecutivos
print(datos['Monica':'Angelica'])
#Elementos no consecutivos
print(datos[['Carlos','Esteban','Monica']])