#El usuario introduce dos palabras con igual numero de caracteres (validar que así sea), se crea una palabra
#combinada con las dos donde se toma 1 carácter de la primera y 1 carácter de la segunda hasta terminar ambas
#palabras, además mostrar el número de caracteres de las palabras.
#Palabra 1 ? Alegre
#Palabra 2 ? Triste
#Combinadas: ATlreigsrtee


#Nota: Yo se que no lo hice de la mejor manera, me gano el estres pero tratare de corregirlo
#Al menos funciona como en el ejemplo

p1 = str.lower(input('dame una palabra1: '))
p2 = str.lower(input('dame una palabra2: '))
comb = p1 + p2
if len(p1) == len(p2) :
    print('Igual numero de caracteres')
else:
    print('Error')
print (f'Numero de caracteres de las palabras combinadas: {len(comb)} caracteres ')

a = (p1[:1])
a1 = (p2[:1])
b = (p1[1:2])
b1 = (p2[1:2])
c = (p1[2:3])
c1 = (p2[2:3])
d = (p1[3:4])
d1 = (p2[3:4])
f = (p1[4:5])
f1 = (p2[4:5])
g = (p1[5:6])
g1 = (p2[5:6])
h = (p1[6:7])
h1 = (p2[6:7])
i = (p1[7:8])
i1 = (p2[7:8])
j = (p1[8:9])
j1 = (p2[8:9])
k = (p1[9:10])
k1 = (p2[9:10])
l = (p1[9:10])
l1 = (p2[9:10])
mez =  a+a1+b+b1+c+c1+d+d1+f+f1+g+g1+h+h1+i+i1+j+j1+k+k1+l+l1
print (mez)