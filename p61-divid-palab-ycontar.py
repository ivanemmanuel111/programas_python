# dividir en palabras y contar
txt = ''' Al año los murcielagos huyen de la fuerte \
luz que baja por el kiosko de wivex
'''

print(f'{len(txt)} - {txt}\n')

palabras = txt.split()
for palabra in palabras:
    print(f'{len(palabra):>4} - {palabra :<25}  ', end=' ')
    v=c=0 #>4 para que quede la tabla pareja
    for car in palabra:
        if car.isalpha():
            if car in 'aeiou': v+=1
            else: c+=1
    print(f'v: {v:>6}, c: {c:>6}')
