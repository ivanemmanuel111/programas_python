#programa importante

import pandas as pd
datos = pd.read_csv('edades.csv',header = None, index_col = 0).squeeze(1)
datos.name = 'Edades'

#print(datos)
#iterar con un ciclo for sobre los datos de la serie
print(datos.name, datos.size)

for nombre, edad in datos.items():
    print(f'Nombre: {nombre:<12} Edad: {edad:>2}')