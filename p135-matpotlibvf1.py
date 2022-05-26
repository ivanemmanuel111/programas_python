import pandas as pd
import matplotlib.pyplot as plt
import os

os.system('clear')

fifa = pd.read_csv('players_21.csv')
#print(fifa.shape)

# Histograma / Edad
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
# Un histograma es útil para ver la distribución de una variable, es decir, nos permite ver los valores más comunes.

dg = fifa['age']
#rint(dg)
plt.figure(figsize=(10,6))
plt.title('Histograma de Edad')
plt.xlabel('Edad')
plt.ylabel('Numero de Jugadores')
plt.hist(dg, color='green')
# plt.show()
plt.close()


# Barras / Valor en Euros ( 5 )
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
# Un gráfico de barras es útil para comparar una variable entre distintos grupos o categorías.

dg = fifa[['short_name','value_eur']].sort_values(ascending=False, by='value_eur').iloc[0:15]
#print(dg)
plt.figure(figsize=(10,8))
plt.title('Barras del valor en Euros')
plt.xlabel('Jugador')
plt.ylabel('Valor en Euros')
plt.tick_params(rotation=45)
plt.bar(dg.short_name, dg.value_eur, color='cyan', edgecolor='blue', hatch='/')
#plt.show()
plt.close()

# Barras horizonal / Jugadores por nacionalidad
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html
# Un gráfico de barras es útil para comparar una variable entre distintos grupos o categorías.

dg = fifa['nationality'].value_counts().sort_values(ascending=False).iloc[0:15]
#print(dg)
plt.figure(figsize=(10,8))
plt.title('Jugadores por nacionalidad', fontsize=25)
plt.xlabel('No de Jugadores')
plt.ylabel('Nacionalidad')
plt.barh(dg.index, dg.values, color=['red','blue'], edgecolor='black', hatch='+')
#plt.show()
plt.close()


# Pastel / Jugadores por Club - salario en euros
# Un gráfico circular se usa para mostrar la relación porcentual entre las partes con relación a su conjunto
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html

dg = fifa.groupby('club_name').sum()['wage_eur'].sort_values(ascending=False).head(8)
#print(dg)
plt.title('Salario en Euros x Club')
plt.pie(dg.values, labels=dg.index, autopct='%1.0f%%', explode=(0.1,0.1,0,0,0,0,0,0), shadow=True, startangle=90)
plt.legend(dg.index, loc='best')
#plt.show()
plt.close()

# Boxplot / Rendimiento de los jugadores
# Los diagramas de cajas son útiles para representar grupos de datos y compararlos entre ellos.
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html

dg = fifa[fifa['club_name']=='Real Madrid']['overall']
#print(dg)
plt.title('Rendimiento General de los Jugadores')
plt.ylabel('Rendimiento')
plt.boxplot(dg)
#plt.show()
plt.close()

# scatter / Edad vs Rendimiento
# El gráfico de dispersión o scatter, sirve para representar la relación entre dos variables
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

dg = fifa[['age','overall']]
#print(dg.shape)
plt.title('Edad vs Rendimiento')
plt.xlabel('Edad')
plt.ylabel('Rendimiento')
plt.scatter(dg.age, dg.overall)
#plt.show()
plt.close()

# hexbin / Edad vs Potencial
# Muestra la relacion entre dos variables
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hexbin.html

dg = fifa[['age','potential']]
#print(dg.shape)
plt.title('Edad vs Potencial')
plt.xlabel('Edad')
plt.ylabel('Potencial')
plt.hexbin(dg.age, dg.potential, gridsize=30)
plt.colorbar()
plt.show()



