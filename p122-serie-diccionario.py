#con diccionario

import pandas as pd
edades = {'Juan':40, 'Pedro':20, 'Maria':36, 'Francisco':20, 'Luis':34}
datos = pd.Series(edades)
datos.name = 'Edades'
print(datos)
#imprime
# Juan 40
# Pedro 20
# Maria 36
# Francisco 20
# Luis 34