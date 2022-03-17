#Leer un número de mes (ej 4).
#Imprimir: días del mes, y nombre del mes (ej marzo, 30).
#Asume 28 para febrero, guarda días en una lista, y nombres de mes en otra

mes = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
dias = [31,28,31,30,31,30,31,31,30,31,30,31]
e = int(input('Dame un num de mes (enero es 0 y diciembre es 11) '))
print(f'Corresponde al mes: {mes[e]} ')
print (f'Tiene {dias[e]} dias')