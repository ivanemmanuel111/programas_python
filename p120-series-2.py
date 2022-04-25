
#Ahora con letras y propias etiquetas
import pandas as pd

a = [1, 7, 2]
miserie = pd.Series(a, index = ['x', 'y', 'z'])
#una letra por cada numero
print(miserie)
#imprime
#x 1
#y 7
#z 2
print(miserie['y'])