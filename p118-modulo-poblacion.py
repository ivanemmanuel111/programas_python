
import p118procesarpoblacion as p

poblacion = [
{'pais':'Colombia','poblacion_2018':49661,'poblacion_2019':50339,'poblacion_2020':50883,'poblacion_2021':51266},
{'pais':'El Salvador','poblacion_2018':6421,'poblacion_2019':6454,'poblacion_2020':6486,'poblacion_2021':6518},
{'pais':'Mexico','poblacion_2018':126191,'poblacion_2019':127576,'poblacion_2020':128933,'poblacion_2021':130262},
{'pais':'Panama','poblacion_2018':4177,'poblacion_2019':4246,'poblacion_2020':4315,'poblacion_2021':4382},
{'pais':'Uruguay','poblacion_2018':3449,'poblacion_2019':3462,'poblacion_2020':3474,'poblacion_2021':3485}
]

# Programa principal

print('\nPor nombres en orden por pais: \n')
p.imprime(poblacion,'pais',False)
print('\nListado de la poblacion ordenado por la Poblacion 2020 en forma descendente: \n')
p.imprime(poblacion,'poblacion_2020',True)

# mayor y menor segun la poblacion en 2018
may = p.valor_mayor(poblacion,'poblacion_2018')
men = p.valor_menor(poblacion,'poblacion_2018')
p.valor_mayor(poblacion,'poblacion_2018')
print('\nPais con la mayor poblacion en el 2018: \n')
p.imprime(may,'',False)
print('\nPais con la menor poblacion en el 2018: \n')
p.imprime(men,'',False)

# mayor y menor segun la poblacion en 2021
may = p.valor_mayor(poblacion,'poblacion_2021')
men = p.valor_menor(poblacion,'poblacion_2021')
p.valor_mayor(poblacion,'poblacion_2021')
print('\nPais con la mayor poblacion en el 2021: \n')
p.imprime(may,'',False)
print('\nPais con la menor poblacion en el 2021: \n')
p.imprime(men,'',False)

