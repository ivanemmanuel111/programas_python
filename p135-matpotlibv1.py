#Graficar con archivos csv

import pandas as pd

import matplotlib.pyplot as plt #Se instalo

import os
os.system('cls')

fifa = pd.read_csv('players_21.csv')
print(fifa.shape)

#Histograma / Edad
dg = fifa['age']
#rint(dg)
plt.figure(figsize=(10,6))
plt.title('Histograma de Edad')
plt.xlabel('Edad')
plt.ylabel('Numero de Jugadores')
plt.hist(dg, color='green')

#plt.show() #muestra la grafica quitar el asterisco para que se muestre
plt.close()

#Barras / Valor en Euros ()
dg = fifa[['short_name', 'value_eur']].sort_values(ascending=False, by='value_eur').iloc[0:15]

plt.figure(figsize=(10,8))
plt.title('Barras de valor en Euros')
plt.xlabel('Jugador')
plt.ylabel('Valor en Euros')
plt.tick_params(rotation=45)
plt.bar(dg.short_name, dg.value_eur, color= 'cyan', edgecolor='blue', hatch='/')

#plt.show() #muestra la grafica
plt.close()

#Barras Horizontal / Jugadores por nacionalidad
dg = fifa['nationality'].value_counts().sort_values(ascending=False).iloc[0:15]

plt.figure(figsize=(10,8))
plt.title('Jugadores por nacionalidad', fontsize=25)
plt.xlabel('No de jugadores')
plt.ylabel('Nacionalidad')
plt.barh(dg.index, dg.values, color= ['red', 'blue'], edgecolor='black', hatch='+')

#plt.show()
plt.close()

#Pastel / jugadores por club - salario en euros
dg = fifa.groupby('club_name').sum()['wage_eur'].sort_values(ascending=False).head(8)

plt.title('Salario en Euros x Club')
plt.pie(dg.values, labels=dg.index, autopct='%1.0f%%', explode=(0.1, 0.1, 0,0,0,0,0,0), shadow=True)
plt.legend(dg.index)

#plt.show()
plt.close()

#Hexbin / Edad vs Potencial

dg = fifa[['age','potential']]

plt.tittle('Edad vs Potencial')

plt.xlabel('Edad')
plt.ylabel('Potencial')
plt.hexbin(dg.age, dg.potential, gridsize=30)
plt.colorbar()
plt.show
plt.close()
