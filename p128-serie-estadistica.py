#programa importante

import pandas as pd
datos = pd.read_csv('edades.csv',header = None, index_col = 0).squeeze(1)
datos.name = 'Edades'
print(datos)

# estadistica descriptiva
print( datos.describe(), '\n')
#obtener datos estadisticos especificos
print('La moda', datos.mode())

print( datos.count() ) # Cuenta
print( datos.mean() ) # Media
print( datos.std() ) # Desv estandar
print( datos.min() ) # Minimo
print( datos.quantile(q=0.25) ) # Quartil 25%
print( datos.quantile(q=0.50) ) # Quartil 50%
print( datos.quantile(q=0.75) ) # Quartil 75%
print( datos.max() ) # Maximo
print( datos.mode() ) 