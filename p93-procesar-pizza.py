# Procesar pizza
#Simular la compra de una pizza

ingr = {'T':1.50, 'P':3.50, 'C':3.74, 'A':0.40} #Letra inicial de ingrediente y precio

base = 15
st = 0 #subtotal
tot = 0
pedido = input('Ingredientes de tu pizza ? ').upper()
for i in pedido:
   if i in 'TPCA': #solo acepta esas letras esto es importante
     st = st + ingr[i]
st = st + base

if st >=20 : 
   tot = st - (st * 0.05) #Descuento
print(f'El subtotal es : {st}')
print(f'El total es : {tot}') 