#programa importante

import pandas as pd
datos = pd.read_csv('edades.csv',header = None, index_col = 0).squeeze(1)
datos.name = 'Edades'

print(datos)
#Atributos
print(datos.name) #nombre de la serie
print(datos.size) # número de elementos
print(datos.index) # etiquetas o indices
print(datos.values) # valores de la serie

