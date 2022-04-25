import pandas as pd

a = [1, 7, 2]
miserie = pd.Series(a) #lo verde lo llamamos de la libreria pandas

print(miserie)
#imprime
#0 1
#1 7
#2 2
print(miserie[0])
#imprime 1
print(miserie[1])
#imprime 7