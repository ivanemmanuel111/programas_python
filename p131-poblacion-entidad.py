import pandas as pd 

#1Leer un archivo delimitado los datos de la poblacion por entidad
datos = pd.read_csv('poblacion.csv', header=None, index_col=0).squeeze(1)
datos.name = 'Poblacion'

#2Toda la serie
print('Trabajando con los datos de la serie completa \n')
print('Orden original', datos, '\n')
print('Orden inverso', datos[::-1], '\n')
print('Orden ascendente por indice ', datos.sort_index(ascending=True), '\n')
print('Orden descendente por valor ', datos.sort_values(ascending=False), '\n')

#3Atributos de la serie
print('Los atributos de la serie \n')
print(f'Nombre: {datos.name} , Tamaño; {datos.size} , Tipo: {datos.dtype} , Bytes: {datos.nbytes}, Tamaño de dato: {datos.nbytes // datos.size} ')

#4Iterar sobre los valores individuales de la serie
print('Iterarando sobre los valores individuales de la serie \n')
for e, p in datos.items():
    print(f'La entidad  {e} tiene una poblacion de {p} persomas')

#5Acceso a datos por indice numerico
print('Ejemplos de acceso a datos por indice numerico \n')
print('Los primeros 5 ', datos[:5], '\n')
print('Los ultimos 5 ', datos[-5:], '\n')
print('Consecutivos ', datos[4:9], '\n')
print('Salteados ', datos[[5,10,15,20]], '\n')

#6Acceso a datos por indice alfabetico
print('Ejemplos de acceso a datos por indice alfabetico \n')
print('Los primeros 5 ', datos[:'Coahuila'], '\n')
print('Los ultimos 5 ', datos['Tamaulipas':], '\n')
print('Consecutivos ', datos['Jalisco':'Oaxaca'], '\n')
print('Salteados ', datos[['Zacatecas','Durango','Aguascalientes','Puebla']], '\n')

#7Filtrar datos
print('Ejemplos de filtrado de datos en serie \n')
print('Los primeros 5 ', datos.head(5), '\n')
print('Los ultimos 5 ', datos.tail(5), '\n')
print('Valor>300 ', datos[datos>300].sort_values(ascending=False), '\n')
print('Valores entre 10 y 100 ', datos[(datos>=10) & (datos<=100)].sort_values())

#8Estadisticas
print('Estadistica descriptiva de los datos de la serie \n')
print('Resumen estadistico ' , datos.describe())
print(f'Media: {datos.mean()}, Desviacion: {datos.std()}, Minimo: {datos.min()}, Maximo: {datos.max()}')
print(f'Q25: {datos.quantile(q=0.25)} , Q50: {datos.quantile(q=0.50)} , Q75: {datos.quantile(q=0.75)}')
print('Moda: ' , datos.mode())

#9Otras operaciones con los datos de la serie
print('La suma de todos              : ', datos.sum())
print('La suma de los primeros 10    : ', datos.head(10).sum())
print('La media 3 salteados          : ', datos[['Zacatecas', 'Jalisco', 'Puebla']].mean())
print('La desviacion salteados       : ', datos[['Zacatecas', 'Jalisco', 'Puebla']].std())
print('Incremento del 10%            : ', datos*0.1)
print('Suma 20 a todos               : ', datos+20)

datosconel10 = datos+20

datosconel10.to_csv('poblacion10.csv')