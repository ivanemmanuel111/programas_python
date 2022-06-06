
import pandas as pd
import matplotlib.pyplot as plt
import os 
import numpy as np

os.system('clear')

fifa = pd.read_csv('players_21.csv')

rm = fifa.query("club_name=='Real Madrid'")
br = fifa.query("club_name=='FC Barcelona'")
jv = fifa.query("club_name=='Juventus'")
lp = fifa.query("club_name=='Liverpool'")

print(fifa.shape, rm.shape, br.shape, jv.shape, lp.shape)

# Gráficas cara a cara misma figura

plt.figure(figsize=(10,8))
plt.title('Histograma de Edad')
plt.xlabel('Edad')
plt.ylabel('Número de Jugadores')
plt.hist(rm.age, color='cyan', density=False, label='RM')
plt.hist(br.age, color='red', density=False, label='BR')
plt.legend(loc='upper right')
#plt.savefig('histograma.png')
#plt.show()
plt.close() 

# Barras / Jugadores mas valiosos

dgrm = rm['value_eur'].sort_values(ascending=False).iloc[0:5]
dgbr = br['value_eur'].sort_values(ascending=False).iloc[0:5]

n = dgrm.shape[0]
sp = np.arange(n)
w = 0.3

plt.figure(figsize=(10,8))
plt.title('Valor en Euros')
plt.xlabel('Jugador')
plt.ylabel('Valor Euros')
plt.bar(sp, dgrm, w, color='red', edgecolor='blue', label='RM')
plt.bar(sp + w, dgbr, w, color='blue', edgecolor='blue', label='BR')
plt.legend()
plt.xticks(sp,['Jugador 1','Jugador 2','Jugador 3','Jugador 4','Jugador 5'])
#plt.show()
plt.close()

# Boxplot / Rendimento 
plt.figure(figsize=(10,8))
plt.title('Rendimiento General de los Jugadores')
plt.ylabel('Rendimento')
sp = np.arange(2)
dg = [rm.overall, br.overall, jv.overall, lp.overall]
plt.boxplot(dg, labels=['RM','BR','JV','LP'])
#plt.show()
plt.close()
 

# Poner graficas en un plot diferente box

# Pie / Jugadores por País

dgrm = rm.nationality.value_counts()
dgbr = br.nationality.value_counts()
dgjv = jv.nationality.value_counts()
#print(dgrm, dgbr, dgjv)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12,6))
fig.suptitle('Jugadores por País')
plt.subplots_adjust( wspace=0.3 )
ax1.title.set_text('Real Madrid')
ax1.pie(labels=dgrm.index, x=dgrm.values, autopct='%1.0f%%', startangle=90, shadow=True)
ax2.title.set_text('FC Barcelona')
ax2.pie(labels=dgbr.index, x=dgbr.values, autopct='%1.0f%%', startangle=90, shadow=True)
ax3.title.set_text('Juventus')
ax3.pie(labels=dgjv.index, x=dgjv.values, autopct='%1.0f%%', startangle=90, shadow=True)
#plt.show()
plt.close()


# scatter - Edad vs rendimiento  
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

fig, ax = plt.subplots(2,2, constrained_layout=True, figsize=(10,8))
fig.suptitle('Edad vs Rendimiento', size=18)
fig.supxlabel('Edad')
fig.supylabel('Rendimiento')
ax[0,0].set_title('Real Madrid')
ax[0,0].scatter(rm.age, rm.overall)
ax[0,1].set_title('FC Barcelona')
ax[0,1].scatter(br.age, br.overall)
ax[1,0].set_title('Juventus')
ax[1,0].scatter(jv.age, jv.overall) 
ax[1,1].set_title('Liverpool')
ax[1,1].scatter(lp.age, lp.overall)
#plt.show()
plt.close()


# hexbin / Edad vs Potencial

fig = plt.figure(figsize=(10,8))
fig.suptitle('Edad vs Potencial')

ax1 = fig.add_subplot(2,2,1)
ax1.set_title('Real Madrid')
im1 = ax1.hexbin(rm.age,rm.potential, cmap="Blues", gridsize=20)
fig.colorbar(im1)

ax2 = fig.add_subplot(2,2,2)
ax2.set_title('Barcelona')
im2 = ax2.hexbin(br.age,br.potential, cmap="Greens", gridsize=20)
fig.colorbar(im2)

ax3 = fig.add_subplot(2,2,3)
ax3.set_title('Juventus')
im3 = ax3.hexbin(jv.age, jv.potential, cmap="Purples", gridsize=20)
fig.colorbar(im3)

ax4 = fig.add_subplot(2,2,4)
ax4.set_title('Liverpool')
im4 = ax4.hexbin(lp.age, lp.potential, cmap="Oranges", gridsize=20)
fig.colorbar(im4)

plt.show()
plt.close()