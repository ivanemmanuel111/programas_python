#Dados los siguientes nombres: • Juan, Maria, Pedro, Jose, Rocio • Pedro, Juan, Pablo, Mateo, Esther • Crea dos conjuntos uno para cada lista de nombres y muestralos ( A, B )
#• Calcula y muestra: ! union de los conjuntos ( A | B) ! intesección de los conjuntos ( A & B) ! diferenia de los conjuntos ( A – B )
#! diferencia simetrica de los conjuntos ( A ^ B ) • Calcula y muestra también ! si el conjunto de nombres Pablo, Mateo, es subconjunto de B
#! si el conjunto A, es superconjunto del conjunto de nombres: Reynaldo, Angelica ! si Pedro esta en A! si Lilia no esta en B

a = {'Juan', 'Maria','Pedro','Jose', 'Rocio'}
b = {'Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther'}
print(f'Conjunto 1: {a} Conjunto 2 : {b}')

c3 = a.union(b)
c4 = a.intersection(b)
c5 = a.difference(b)
c6 = a.symmetric_difference(b)
print(f'\nUnion {c3}, interseccion {c4}, diferencia {c5}, diferencia simetrica {c6}')

c7 = {'Pablo', 'Mateo'}
c8 = {'Reynaldo', 'Angelica'}
print(f"c7:{c7} es subconjunto de b:{b} : {c7.issubset(b)} {c7<=b} ")
print(f"a:{a} es superconjunto de c8:{c8} : {a.issuperset(c8)} {a>=c8}")
print(f" Pedro esta en {a} ? : {'Pedro' in a}")
print(f" Lilia no esta en {b} ? : {'Lilia' not in b}")


