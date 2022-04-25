#programa importante

import pandas as pd
datos = pd.read_csv('edades.csv',header = None, index_col = 0).squeeze(1)
datos.name = 'Edades'
print(datos)

# estadistica descriptiva
print( datos.describe(), '\n')
#hacer operaciones especificas
print( datos.sum(), '\n') # la suma de todas las edades

print( datos[0:3].sum(), '\n') # suma edades de 0 a 3

print( datos[['Angelica','Claudia']].sum(), '\n') # suma edades Juan y Pedro
print( datos['Pedro':'Sandra'].sum(), '\n') # suma edades Juan y Pedro
print( datos[[0,2,4]].mean(), '\n') # media de indices 0,2,4
print( datos[2:4].std(), '\n') # desvacion de indices 2,3
print( datos+3, '\n') # suma 3 a todas las edades
print( datos*2, '\n') # multiplica x 2 todas las edades

