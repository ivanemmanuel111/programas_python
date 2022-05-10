import pandas as pd 

#Leer un archivo delimitado los datos de las viviendas por estado
datos = pd.read_csv('vivienda.csv', header=None, index_col=0).squeeze(1)
datos.name = 'Vivienda'

#Toda la serie
print('Trabajando con los datos de la serie completa \n')
print('Orden original', datos, '\n')
print('Orden inverso', datos[::-1], '\n')
print('Orden ascendente por indice ', datos.sort_index(ascending=True), '\n')
print('Orden descendente por indice ', datos.sort_values(ascending=False), '\n')

#Atributos de la serie
print('Los atributos de la serie \n')
print(f'Nombre: {datos.name} , Tamaño; {datos.size} , Tipo: {datos.dtype} , Bytes: {datos.nbytes}, Tamaño de dato: {datos.nbytes // datos.size} ')

#Iterar sobre los valores individuales de la serie
print('Iterarando sobre los valores individuales de la serie \n')
for m, v in datos.items():
    print(f'El municipio de {m} tiene un total de {v} viviendas')

#Acceso a datos por indice numerico
print('Ejemplos de acceso a datos por indice numerico \n')
print('Los primeros 5 ', datos[:5], '\n')
print('Los ultimos 5 ', datos[-5:], '\n')
print('Consecutivos ', datos[4:9], '\n')
print('Salteados ', datos[[5,10,15,20]], '\n')

#Acceso a datos por indice alfabetico
print('Ejemplos de acceso a datos por indice alfabetico \n')
print('Los primeros 5 ', datos[:'Calera'], '\n')
print('Los ultimos 5 ', datos['Villa Hidalgo':], '\n')
print('Consecutivos ', datos['Jalpa':'Loreto'], '\n')
print('Salteados ', datos[['Jerez','Fresnillo','Calera','Pinos']], '\n')

#Filtrar datos
print('Ejemplos de filtrado de datos en serie \n')
print('Los primeros 5 ', datos.head(5), '\n')
print('Los ultimos 5 ', datos.tail(5), '\n')
print('Valor>5000 ', datos[datos>5000].sort_values(ascending=False), '\n')
print('Valores entre 300 y 1200 ', datos[(datos>=300) & (datos<=1200)].sort_values())

#Estadisitcas
print('Estadistica descriptiva de los datos de la serie \n')
print('Resumen estadistico ' , datos.describe())
print(f'Media: {datos.mean()}, Desviacion: {datos.std()}, Minimo: {datos.min()}, Maximo: {datos.max()}')
print(f'Q25: {datos.quantile(q=0.25)} , Q50: {datos.quantile(q=0.50)} , Q75: {datos.quantile(q=0.75)}')
print('Moda: ' , datos.mode())

#Otras operaciones con los datos de la serie
print('La suma de todos              : ', datos.sum())
print('La suma de los primeros 10    : ', datos.head(10).sum())
print('La media ultimos 10           : ', datos.tail(10).mean())
print('La desviacion salteados       : ', datos[['Calera', 'Fresnillo', 'Apulco']].std())
print('Incremento del 10%            : ', datos*0.1)

datosconel10 = datos*0.1

datosconel10.to_csv('viviendas10.csv')