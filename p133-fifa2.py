import pandas as pd
import os
os.system('cls')

# 1. Importar los datos del archivo csv 
fifa21 = pd.read_csv('players_21.csv')

# 2. El DataFrame original

print('Todo el DataFrame :\n\n', fifa21, '\n')
print('Forma             : ', fifa21.shape, '\n')
print('Tamaño            : ', fifa21.size, '\n' )
print('Columnas          :\n\n', fifa21.columns, '\n')

# 3. El DataFrame de reducido

fifa21small = fifa21[['short_name','age','height_cm','weight_kg','nationality', 'club_name','overall', 'potential', 'value_eur', 'wage_eur', 'player_positions','power_jumping','power_long_shots']]

fifasm = fifa21small[ ( fifa21small['club_name']=='Real Madrid' )  |  ( fifa21small['club_name']=='FC Barcelona')]

fifasm.set_index('short_name', inplace=True)

print('Orden orginal : \n', fifasm, '\n')
print('Orden inverso : \n', fifasm[::-1], '\n')
print('Orden ascendente  por indice', fifasm.sort_index(ascending=True), '\n')
print('Orden descendente por valor', fifasm.sort_values(ascending=False, by='age'), '\n')
print('Forma        : ',  fifasm.shape, '\n')
print('Tamaño       : ',  fifasm.size, '\n' )
print('Columnas     :\n', fifasm.columns, '\n')
print('Tipos        :\n\n', fifasm.dtypes, '\n' )

# 4. Iterar sobre el DataFrame

print('\nIterar sobre el DataFrame')

print('Iterar por las columnas: ')
for c,s in fifasm.items():
    print('\nColumna: ',c, '\n')
    print('Serie : \n', s)

print('\nIterar por los renglones y columnas v1 :')
print('Estatura, peso, nacionalidad: \n')
for i,r in fifasm.iterrows():
    print(i,'mide',r['height_cm'],'cm y pesa',r['weight_kg'],'kg','es de nacionalidad',r['nationality'])

print('\nIterar por lo renglonse y  columnas v2')
for r in fifasm.itertuples():
    print(r,'\n')

# 5. Acceder a una Serie del DataFrame
print('\nAcceder una Serie por indice alfabetico o nombre) \n')
print('Valore en euros     :\n',fifasm['value_eur'].sort_values(ascending=False) , '\n')
print('Rendimiento general :\n',fifasm.overall.sort_values(ascending=False) , '\n')
print('Los 10 primeros, todas las Series:\n', fifasm.head(10),'\n')
print('Los 10 ultimos, todas las Series  :\n', fifasm.tail(10),'\n')
print('Acceder al tope y cola de una sere específica:\n')
print('Primeros 10 de una serie    :\n\n', fifasm['age'].head(10), '\n')
print('Ultimos  10 de una serie    :\n\n', fifasm.wage_eur.tail(10), '\n')

# 6. Acceder por índice numérico

print('\nAcceder por índice numérico: \n\n')
print('\nAcceder renglones usando indice numérico: \n')
print('Acceder renglón : \n',fifasm.iloc[3])
print('\nAcceder renglones continuos: \n')
print( fifasm.iloc[2:5] )
print('\nAcceder renglones dispersos:\n')
print( fifasm.iloc[[1,3,5]] )
print('\nAcceder renglones alternados \n')
print( fifasm.iloc[0:10:2] )

print('\nAcceder columnas por indice numérico: \n')
print('Acceder columna')
print( fifasm.iloc[:,0])
print('Acceder columnas contínuas: \n')
print( fifasm.iloc[:,0:3])
print('Acceder columnas dispersas:\n')
print( fifasm.iloc[:,[0,3]])
print('Acceder columnas alternadas:\n')
print( fifasm.iloc[:,0:6:2])

# 7. Acceder por índice alfabético

print('\nAcceder rebglones por indice alfabético: \n')

print('\nAcceder renglón  \n')
print(fifasm.loc['Marcelo'])
print('\nAcceder renglones continuos \n')
print(fifasm.loc['Casemiro':'Carvajal'])
print('\nAcceder a renglones dispersos\n')
print(fifasm.loc[['Isco','Mariano','Belman']])
print('\nAcceder renglones alternados: \n')
print(fifasm.loc['T. Courtois':'Marcelo':2])

print('\nAcceder columnas por indice alfabético: \n')

print('\nAcceder columna específica \n')
print(fifasm.loc[:,'age'])
print('Acceder columnas consecutivas')
print( fifasm.loc[:,'age':'club_name'])
print('Acceder columnas dispersas')
print( fifasm.loc[:,['power_jumping','age','overall']])
print('Acceder columnas alternadas')
print( fifasm.loc[:,'age':'club_name':2])

# 8. Acceder elemento  

print('\nAcceder elemento : \n')

print(fifasm)
print('\nAcceder elemento por indice numérico: \n')
print('Primer renglon y primera columna : ', fifasm.iat[0,0] )
print('Último renglon y ultima columna  : ', fifasm.iat[64,11] )
print('\nAcceder elemento por indice alfabético:  \n')
print('Primer renglon y primera columna : ', fifasm.at['L. Messi','age'] )
print('Último renglon y ultima columna  : ', fifasm.at['Arribas','power_long_shots'] )


# 9. Filtrar datos v1
  
print('\n Fitrar datos v1 : \n')

print('\nFiltrar por un criterio ejemplo 1 \n')
print( fifasm[ fifasm['age'] > 30 ] )
print('\nFiltrar por un criterio ejemplo 2\n')
print( fifasm[ fifasm.player_positions.isin(['LW','ST']) ] )
print('\nFiltrar por un criterio ejemplo 3\n')
print( fifasm[ fifasm['nationality'].str.startswith('B') ] )
print('\nFiltrar por dos criterios\n')
print( fifasm[ (fifasm['age'] < 30) & (fifasm['club_name']=='FC Barcelona') ] )

# 10. Filtrar datos v1

print('\n Fitrar datos v2 : \n')

print('\nFiltrar por un criterio ejemplo 1\n')
print( fifasm.query(' age >= 30 ') )
print('\nFiltrar por un criterio ejemplo 2\n')
print( fifasm.query(" nationality != 'Brazil' ")['nationality'] )
print('\nFiltrar por un criterio ejemplo 3\n')
print( fifasm.query(" nationality in ('Spain','Brazil') ")['nationality']  )
print('\nFiltrar por dos criterios ejemplo 1\n')
print( fifasm.query(" age <= 30 & nationality == 'Spain' " )[['age','nationality']])
print('\nFiltrar por dos criterios ejemplo 2\n')
print(fifasm.query(" weight_kg <= 80 & height_cm >= 180 " ) )
print('\nFiltraren por dos criterios ejemplo 3\n')
print( fifasm.query(" nationality not in ('Spain', 'Portugal') & age <=25 " )[['age','nationality']] )


# 11. Estadistica descriptiva

print('\n Estadistica descriptiva: \n')

print('Estadística descriptiva general:\n')
print(fifasm.describe())
print('\nEstadístca descriptiva indivdual \n')
print('La cuenta      :\n', fifasm.count(), '\n')
print('La Media       :\n', fifasm.mean(numeric_only=True), '\n')
print('La Desviación  :\n', fifasm.std(numeric_only=True), '\n')
print('El mínimo      :\n', fifasm.min(numeric_only=True), '\n')
print('El máximo      :\n', fifasm.max(numeric_only=True), '\n')
print('Q 25%          :\n', fifasm.quantile(q=0.25), '\n')
print('\n Estadistica descriptiva de una Serie: \n')
print(fifasm['age'].describe(), '\n')
print(fifasm.height_cm.describe(), '\n')

# 12 Agrupar datos

print('\nAgrupar datos \n')

print('\nAgrupar por ucolumna ejemplo 1: ')
print(fifasm.groupby('nationality')[['wage_eur','value_eur']].sum().sort_values(ascending=False, by='wage_eur'))
print('\nAgrupar por columna ejemplo 2: ')
print(fifasm.groupby('nationality').mean())
print('\nAgrupar por dos columnas:')
print(fifasm.groupby(['club_name','nationality'])[['wage_eur','value_eur']].sum())

# 13. Operaciones entre Series

print('\nOperaciones entre  Series')

print('\nSuma de Edad y Peso')
print(fifasm.eval(' suma = (age + weight_kg) - height_cm ') )
print('\nCon peso mayor igual a 70 , expresion Boleana')
print( fifasm.eval( 'weight_kg > = 70 ') )
print('\nCon peso mayor al peso promedio ', fifasm.weight_kg.mean())
print(fifasm.eval('weight_kg >= weight_kg.mean()'))
 