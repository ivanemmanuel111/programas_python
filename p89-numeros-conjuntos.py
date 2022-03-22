#Dados los siguientes números: ! 50,60,70,80,90,100,200 ! 60,90,100,300,400,500 ! 10,20,60,90,70,100,600,700 • Crear tres conjuntos, uno por cada lista de números y mostrarlos ( A, B, C)
#• Calcula y muestra: ! union de los conjuntos A y B ( A | B ) ! union de los conjuntos B y C ( B | C )! diferencia de A y C ( A – C)
#! diferencia simétrica de B y C ( B ^ C) ! intersección de B y C ( B & C ) • Calcula y responda a las siguientes preguntas>
#! A es subconjunto de B ? ! C es subconjunto de A ? ! 100 esta en A ? ! 60 esta en A , y en B y en C ? ! 900 no esta en C ?


a = {50,60,70,80,90,100,200}
b = {60,90,100,300,400,500}
c = {10,20,60,90,70,100,600,700}
print(f'conjunto a : {a}, conjunto b : {b}, conjunto c: {c}')

c1 = a.union(b)
c2 = b.union(c)
c3 = a.difference(c)
c4 = b.symmetric_difference(c)
c5 = b.intersection(c)
print(f'\nUnion a y b {c1}, union b y c {c2}, diferencia a y c {c3}, diferencia simetrica b y c {c4}, interseccion b y c {c5}')

print(f"a:{a} es subconjunto de b:{b} : {a.issubset(b)} {a<=b} ")
print(f"c:{c} es subconjunto de a:{a} : {c.issubset(a)} {c<=a} ")
print(f" 100 esta en {a} ? : {100 in a}")
print(f" 60 esta en {a} , y en {b} y en {c} ? : {60 in a} {60 in b} {60 in c}")
print(f" 900 no esta en {c} ? : {900 not in c}")