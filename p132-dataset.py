import pandas as pd
# Crear varias series en base a listas
nombre = pd.Series(["Juan", "Pedro", "Luis", "Maria", "Genaro", "Israel", "Fatima", "Angelica", "Ancelmo"])
#decirle a pandas que me la convierta en serie

edad = pd.Series([33, 35, 35, 30, 25, 34, 42, 22, 55])
peso = pd.Series([45, 65.5, 30.5, 80, 45, 25, 60, 45, 90])
ojos = pd.Series(['Cafe','Verde','Azul','Negro','Cafe','Verde','Azul','Negro','Negro'])
estatura = pd.Series([1.22, 1.70, 1.80, 1.66, 1.50, 1.90, 1.33, 1.75, 1.80])
promedio = pd.Series([8.5, 7.0, 6.5, 10, 9.5, 5, 8, 7.5, 5])
municipio = pd.Series(['Jerez','Fresnillo','Rio Grande','Panfilo Natera','Zacatecas','Jerez','Fresnillo','Panfilo Natera','Fresnillo'])

# Crear DataFrame en base a las series
df = pd.DataFrame(data={"Nombre":nombre, "Edad":edad, "Peso":peso, "Ojos":ojos, "Estatura":estatura, "Promedio":promedio, "Municipio":municipio })
df.set_index('Nombre', inplace=True)
# Imprimir los datos del DataFrame
print(df, '\n')
#Atributos
print('Informacion de la serie   :\n', df.info(),'\n')
print('Indices de la serie       :\n', df.index, '\n')
print('Valores de la serie       :\n', df.values, '\n' )
print('Columnas de la serie      :\n', df.columns, '\n' )
print('Tipos de dato de la serie :\n', df.dtypes, '\n' )
print('Forma de la serie         : ', df.shape, '\n' )
print('Tamaño de la serie        : ', df.size, '\n' )
print('Dimensiones de la serie ? : ', df.ndim, '\n' )
print('La serie esta vacia ?     : ', df.empty, '\n' )
print('Uso de la memoria         :\n', df.memory_usage(), '\n')

# Iterar por los elementos del Dataframe
for columna, serie in df.items():
    print('\nColumna: ', columna, '\n')
    print('Serie :\n', serie)

# Iterar por los renglones del DataFrame
print('\nIterar por los renglons del DataFrame en base al par (indice, serie):\n')
print('Las edades: \n')
for indice, renglon in df.iterrows():
    print(indice, ' tiene ', renglon['Edad'], ' de edad.')

print('\n Iterar por renglones en base tuplas \n')
for ren in df.itertuples(index='Nombre'):
    print(ren)

# Acceder a una serie y sus elementos
print('\nAcceder a una Serie completa por indice alfabetico) \n')
print(df['Edad'] , '\n')
print('\nAcceder a una Serie completa por nombre) \n')
print(df.Edad, '\n')
print('\nAcceder a los elementos del del topoe y la cola del DataSet:\n')
print(df.head(), '\n')
print(df.tail(), '\n')
print('\nAcceder a los elementos del del tope y la cola de una serie específica:\n')
print(df['Promedio'].head(3), '\n')
print(df.Ojos.tail(3), '\n')

# Acceder a los renglones con iloc
print('\nAcceder a un renglón específico con iloc \n')
print(df.iloc[0])
print('\nAcceder a renglones continuos con iloc \n')
print(df.iloc[1:4])
print('\nAcceder a renglones dispersos con iloc \n')
print(df.iloc[[1,3,5]])
print('\nAcceder a renglones alternados (uno si y uno no) con iloc\n')
print(df.iloc[0:9:2])

# Acceder a las columnas con iloc
print('Acceder a una columna con iloc')
print( df.iloc[:,0])
print('Acceder columnas consecutivas iloc')
print( df.iloc[:,0:2])
print('Acceder columnas dispersas iloc')
print( df.iloc[:,[0,3]])
print('Acceder columnas alternadas')
print( df.iloc[:,0:7:2])

# Acceder a los renglones con loc
print('\nAcceder a un renglón específico con loc \n')
print(df.loc['Juan'])
print('\nAcceder a renglones continuos con loc \n')
print(df.loc['Juan':'Luis'])
print('\nAcceder a renglones dispersos con loc \n')
print(df.loc[['Juan','Genaro','Ancelmo']])
print('\nAcceder a renglones alternados (uno si y uno no) con loc\n')
print(df.loc['Juan':'Ancelmo':2])

# Acceder a las columnas con loc
print('Acceder a una columna con iloc')
print( df.loc[:,'Promedio'])
print('Acceder columnas consecutivas loc')
print( df.loc[:,'Edad':'Ojos'])
print('Acceder columnas dispersas loc')
print( df.loc[:,['Edad','Ojos','Promedio']])
print('Acceder columnas alternadas')
print( df.loc[:,'Edad':'Municipio':2])

# Acceder elemento específico del DataFrame con iat
print('\nAcceder a elementos específico del DataFrame con iat \n')
print('\nEl primer renglon y primera columna (Edad de Juan) : ', df.iat[0,0] )
print('\nEl ultimo renglon y ultima columna (Municipio de Ancelmo) : ', df.iat[8,5] )
print('\nAcceder a elementos específico del DataFrame con at \n')
print('\nEl primer renglon y primera columna (Edad de Juan) : ', df.at['Juan','Edad'] )
print('\nEl ultimo renglon y ultima columna (Municipio de Ancelmo) : ', df.at['Ancelmo','Municipio'])

# Filtrar datos en el DataFrame directamente
print('\nFiltrar por un criterio ejemplo 1 \n')
print(df[ df['Edad'] > 30 ])
print('\nFiltrar por un criterio ejemplo 2\n')
print(df[ df.Municipio.isin(['Fresnillo','Jerez']) ])
print('\nFiltrar por un criterio ejemplo 3\n')
print(df[ df['Ojos'].str.startswith('V') ])
print('\nFiltrar en base a dos criterios\n')
print(df[ (df['Edad'] > 30) & (df['Ojos']=='Verde') ])

# Filtrar datos en el DataSet con query
print('\nFiltrar por un criterio ejemplo 1\n')
print(df.query("Edad > 30") )
print('\nFiltrar por un criterio ejemplo 1\n')
print(df.query("Ojos != 'Verde'") )
print('\nFiltrar por un criterio ejemplo 3\n')
print(df.query("Municipio in ('Zacatecas','Panfilo Natera')") )
print('\nFiltrar por dos criterios a la vez ejemplo 1\n')
print(df.query(" Edad > 30 & Ojos=='Verde' " ))
print('\nFiltrar por dos criterios a la vez ejemplo 2\n')
print(df.query(" Estatura >= 1.70 & Estatura <= 1.80 " ))
print('\nFiltrar por dos criterios a la vez ejemplo 3\n')
print(df.query(" Municipio not in ('Fresnillo','Panfilo Natera') & Edad <=25" ))

# Estadisticas en el DataFrame
print('\n Estadistica descriptiva del DataFrame: \n')
print(df.describe())
print('\nEstadístca descriptiva indivdual \n')
print('La cuenta :\n', df.count(), '\n')
print('La Media :\n', df.mean(numeric_only=True), '\n')
print('La Desviación :\n', df.std(numeric_only=True), '\n')
print('El mínimo :\n', df.min(), '\n')
print('El máximo :\n', df.max(), '\n')
print('Q 25% :\n', df.quantile(q=0.25), '\n')
print('\n Estadistica descriptiva de una Serie: \n')
print(df['Edad'].describe(), '\n')
print(df.Estatura.describe(), '\n')

# Operaciones sobre el DataFrame
print('\nLa suma del DataFrame: \n')
print(df.sum(numeric_only=True))
print('\nLa suma del de una Serie específica del DataFrame: \n')
print('La suma del Peso : ', df.Peso.sum())
print('La suma de la Edad: ', df['Edad'].sum())
print('\nLa desviación estandar de datos específicos del DataFrame \n')
print('\nLa desvición de los primeros 5')
print(df.head().std(numeric_only=True))
print('\nLa desviacíon de Juan hasta Gerardo')
print(df.loc['Juan':'Genaro'].std(numeric_only=True))
print('\nLa desviacíon de Estatura y Promedio')
print( df.loc[:,['Estatura','Promedio']].std(numeric_only=True))

# Operacions sobre el DataFrame agrupar
print('\nAgrupar datos \n')
print('\nAgrupar por una columna: ')
print(df.groupby('Ojos').sum())
print('\nAgrupar en base a dos columnas:')
print(df.groupby(['Municipio','Ojos']).mean())

# Otras operaciones sobre el DataFrame con eval
print('\nOperaciones sobre el DataFrame con eval')
print('\n Suma de Edad y Peso')
print(df.eval('Suma = Edad + Peso') )
print('\nCon peso mayor a 70, expresion Boleana')
print(df.eval('Peso>70'))
print('\nCon edades mayores a la edad promedio ', df.Edad.mean())
print(df.eval('Edad >= Edad.mean()'))



