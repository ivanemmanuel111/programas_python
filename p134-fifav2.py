#Fifa v2 Datafream

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

fifa21small = fifa21[['short_name', 'age', 'height_cm', 'weight_kg', 'nationality', 'club_name', 'overall', 'potential', 'value_eur', 'wage_eur', 'player_positions', 'preferred_foot', 'shooting', 'passing', 'dribbling', 'defending', 'mentality_aggression', 'mentality_interceptions', 'mentality_positioning']]

fifasm = fifa21small[ ( fifa21small['club_name']=='Liverpool' )  |  ( fifa21small['club_name']=='Juventus')  |  ( fifa21small['club_name']=='Chelsea')]

fifasm.set_index('short_name', inplace=True)

print('Orden orginal : \n', fifasm, '\n')
print('Orden inverso : \n', fifasm[::-1], '\n')
print('Orden ascendente  por indice', fifasm.sort_index(ascending=True), '\n')
print('Orden descendente por valor', fifasm.sort_values(ascending=False, by='nationality'), '\n')
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
print('Club, Estatura, peso, nacionalidad: \n')
for i,r in fifasm.iterrows():
    print(i,'club',r['club_name'],'mide',r['height_cm'],'cm y pesa',r['weight_kg'],'kg','es de nacionalidad',r['nationality'])

print('\nIterar por lo renglonse y  columnas v2')
for r in fifasm.itertuples():
    print(r,'\n')

# 5. Acceder a una Serie del DataFrame
print('\nAcceder una Serie por indice alfabetico o nombre) \n')
print('Valor de defensa    :\n',fifasm['defending'].sort_values(ascending=False) , '\n')
print('Rendimiento pase    :\n',fifasm.passing.sort_values(ascending=False) , '\n')
print('Los 10 primeros, todas las Series:\n', fifasm.head(10),'\n')
print('Los 10 ultimos, todas las Series  :\n', fifasm.tail(10),'\n')
print('Acceder al tope y cola de una sere específica:\n')
print('Primeros 10 de una serie    :\n\n', fifasm['weight_kg'].head(10), '\n')
print('Ultimos  10 de una serie    :\n\n', fifasm.value_eur.tail(10), '\n')

# 6. Acceder por índice numérico

print('\nAcceder por índice numérico: \n\n')
print('\nAcceder renglones usando indice numérico: \n')
print('Acceder renglón : \n',fifasm.iloc[5])
print('\nAcceder renglones continuos: \n')
print( fifasm.iloc[5:10] )
print('\nAcceder renglones dispersos:\n')
print( fifasm.iloc[[2,4,6]] )
print('\nAcceder renglones alternados \n')
print( fifasm.iloc[0:15:2] )

print('\nAcceder columnas por indice numérico: \n')
print('Acceder columna')
print( fifasm.iloc[:,1])
print('Acceder columnas contínuas: \n')
print( fifasm.iloc[:,1:5])
print('Acceder columnas dispersas:\n')
print( fifasm.iloc[:,[3,5,7]])
print('Acceder columnas alternadas:\n')
print( fifasm.iloc[:,6:10:2])

# 7. Acceder por índice alfabético

print('\nAcceder rebglones por indice alfabético: \n')

print('\nAcceder renglón  \n')
#print(fifasm.loc['Marcelo'])

print('\nAcceder renglones continuos \n')
print(fifasm.loc['C. Jones':'C. Kelleher'])
print('\nAcceder a renglones dispersos\n')
print(fifasm.loc[['Alisson','G. Frabotta','L. Coccolo']])
print('\nAcceder renglones alternados: \n')
print(fifasm.loc['Cristiano Ronaldo':'C. Kelleher':2])

print('\nAcceder columnas por indice alfabético: \n')

print('\nAcceder columna específica \n')
print(fifasm.loc[:,'mentality_interceptions'])
print('Acceder columnas consecutivas')
print( fifasm.loc[:,'age':'nationality'])
print('Acceder columnas dispersas')
print( fifasm.loc[:,['shooting','passing','overall']])
print('Acceder columnas alternadas')
print( fifasm.loc[:,'age':'defending':2])

# 8. Acceder elemento  

print('\nAcceder elemento : \n')

print(fifasm)
print('\nAcceder elemento por indice numérico: \n')
print('Primer renglon y primera columna : ', fifasm.iat[0,0] )
#print('Último renglon y ultima columna  : ', fifasm.iat[97,17] )
print('\nAcceder elemento por indice alfabético:  \n')
print('Primer renglon y primera columna : ', fifasm.at['Cristiano Ronaldo','age'] )
print('Último renglon y ultima columna  : ', fifasm.at['C. Kelleher','mentality_positioning'] )


# 9. Filtrar datos v1
  
print('\n Fitrar datos v1 : \n')

print('\nFiltrar por un criterio ejemplo 1 \n')
print( fifasm[ fifasm['age'] >= 35 ] )
print('\nFiltrar por un criterio ejemplo 2\n')
print( fifasm[ fifasm.player_positions.isin(['CB','ST']) ] )
print('\nFiltrar por un criterio ejemplo 3\n')
print( fifasm[ fifasm['nationality'].str.startswith('B') ] )
print('\nFiltrar por dos criterios\n')
print( fifasm[ (fifasm['age'] < 20) & (fifasm['club_name']=='Juventus') ] )

# 10. Filtrar datos v1

print('\n Fitrar datos v2 : \n')

print('\nFiltrar por un criterio ejemplo 1\n')
print( fifasm.query(' age >= 30 ') )
print('\nFiltrar por un criterio ejemplo 2\n')
print( fifasm.query(" nationality != 'Spain' ")['nationality'] )
print('\nFiltrar por un criterio ejemplo 3\n')
print( fifasm.query(" nationality in ('Sweden','Brazil') ")['nationality']  )
print('\nFiltrar por dos criterios ejemplo 1\n')
#print( fifasm.query("(shooting >= 49 & (shooting <= 89 " ))
print('\nFiltrar por dos criterios ejemplo 2\n')
#print(fifasm.query(" mentality_aggression < 40 & club_name = Juventus " ) )
print('\nFiltraren por dos criterios ejemplo 3\n')
print( fifasm.query(" nationality not in ('Brazil', 'Peru') & passing < 79 " )[['passing','nationality']] )

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
print(fifasm['passing'].describe(), '\n')
print(fifasm.shooting.describe(), '\n')


# 12 Agrupar datos

print('\nAgrupar datos \n')

print('\nAgrupar por ucolumna ejemplo 1: ')
print(fifasm.groupby('passing')[['wage_eur','value_eur']].sum().sort_values(ascending=False, by='wage_eur'))
print('\nAgrupar por columna ejemplo 2: ')
print(fifasm.groupby('shooting').mean())
print('\nAgrupar por dos columnas:')
print(fifasm.groupby(['club_name','nationality'])[['wage_eur','value_eur']].sum())

# 13. Operaciones entre Series

print('\nOperaciones entre  Series')

print('\nSuma de Mentalidades')
#print(fifasm.eval(' suma = (mentality_interceptions + mentality_positioning + mentality_aggression)') )
print('\nCon dribbling mayor igual a 70 , expresion Boleana')
print( fifasm.eval( ' dribbling > = 70 ') )
print('\nCon defending mayor al  defending promedio ', fifasm.defending.mean())
print(fifasm.eval(' defending >=  defending.mean()'))

#Fin del programa

