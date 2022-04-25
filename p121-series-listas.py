#en base a dos listas crear serie

import pandas as pd

indice = ['Juan', 'Pedro', 'Maria', 'Francisco', 'Luis']
valores = [40, 20, 36, 20, 34]
datos = pd.Series(valores, indice)
datos.name = 'Edades'
print(datos)

#imprime
#Juan 40
#Pedro 20
#Maria 36
#Francisco 20
#Luis 34