#Procesar datos fifa

import p116modulofifa as f


fifa = [
{'id':58023,'nombre':'Lionel Andres Messi', 'valeuros': 103500000,'edad':33,'peso': 72,'nacionalidad':'Argentina'},
{'id':20801,'nombre':'Cristiano Ronaldo dos Santos', 'valeuros':63000000,'edad':35,'peso':83,'nacionalidad':'Portugal'},
{'id':188545,'nombre':'Robert Lewandowski','valeuros':111000000,'edad':31,'peso':80,'nacionalidad':'Poland'},
{'id':190871,'nombre':'Neymar da Silva Santos Jr','valeuros':132000000,'edad':28,'peso':68,'nacionalidad':'Brazil'},
{'id':192985,'nombre':'Kevin De Bruyne','valeuros':129000000,'edad':29,'peso':70,'nacionalidad':'Belgium'},
{'id':200389,'nombre':'Jan Oblak','valeuros':120000000,'edad':27,'peso':87,'nacionalidad':'Slovenia'},
{'id':192448,'nombre':'Marc-Andre ter Stegen','valeuros':110000000,'edad':28,'peso':85,'nacionalidad':'Germany'},
{'id':203376,'nombre':'Virgil van Dijk','valeuros': 113000000,'edad':28,'peso':92,'nacionalidad':'Netherlands'},
{'id':208722,'nombre':'Sadio Mane','valeuros':120500000,'edad':28,'peso':69,'nacionalidad':'Senegal'},
{'id':209331,'nombre':'Mohamed Salah Ghaly','valeuros':120500000,'edad':28,'peso':71,'nacionalidad':'Egypt'},
{'id':212831,'nombre':'Alisson Ramses Becker','valeuros':102000000,'edad':27,'peso':91,'nacionalidad':'Brazil'},
{'id':231747,'nombre':'Kylian Mbappe Lottin','valeuros':185500000,'edad':21,'peso':73,'nacionalidad':'France'},
{'id':153079,'nombre':'Sergio Leonel Aguero del Castillo', 'valeuros':83500000,'edad':32,'peso':70,'nacionalidad':'Argentina'},
{'id':155862,'nombre':'Sergio Ramos Garcia','valeuros':33500000,'edad':34,'peso':82,'nacionalidad':'Spain'},
{'id':165153,'nombre':'Karim Benzema','valeuros':83500000,'edad':32,'peso':81,'nacionalidad':'France'},
{'id':167495,'nombre':'Manuel Peter Neuer','valeuros':17500000,'edad':34,'peso':92,'nacionalidad':'Germany'},
{'id':192119,'nombre':'Thibaut Courtois','valeuros':82000000,'edad':28,'peso':96,'nacionalidad':'Belgium'},
{'id':200145,'nombre':'Carlos Henrique Venancio Casimiro','valeuros':90500000,'edad':28,'peso':84,'nacionalidad':'Brazil'}
]

# Programa principal
print('\nPor nombres de menor a mayor: \n')
f.imprime(fifa,'nombre',False)
print('\nPor valor en euros del mayor a menor')
f.imprime(fifa,'valeuros',True)
# mayor y menor segun valor en euros
may = f.valor_mayor(fifa,'valeuros')
men = f.valor_menor(fifa,'valeuros')
f.valor_mayor(fifa,'valeuros')
print('\nJugador con mayor valor en euros: \n')
f.imprime(may,'',False)
print('\nJugador con menor valor en euros: \n')
f.imprime(men,'',False)
# mayor y menor segun edad
may = f.valor_mayor(fifa,'edad')
men = f.valor_menor(fifa,'edad')
f.valor_mayor(fifa,'valeuros')
print('\nJugador con mayor edads: \n')
f.imprime(may,'',False)
print('\nJugador con menor edad: \n')
f.imprime(men,'',False)
# solo los de brazil
nac = [ j for j in fifa if j['nacionalidad']=='Brazil']
print('\nJugadores de Naconalidad Brazil: \n')
f.imprime(nac,'nombre',False)