# calcula lasegunda ley de newton (fuerza = masa * aceleracion)

print('Calculando la segunda ley de newton (f = m * a) ...')
print('Calcular la fuerza .....[f]')
print('Calcular la masa .....[m]')
print('Calcular la aceleracion .....[a]')
op = str.lower(input('Elige una opcion ?'))
if op == 'f' :
    print('\nCalculando la fuerza ...')
    m = float(input('dame la masa ?'))
    a = float(input('dame la aceleracion ?'))
    f = m * a
    print(f'\n La fuerza es {f}')
elif op == 'm' :
    print('\nCalculando la masa ...')
    f = float(input('dame la fuerza ?'))
    a = float(input('dame la aceleracion ?'))
    m = f / a
    print(f'\n La masa es {m}')
elif op == 'a' :
    print('\nCalculando la aceleracion ...')
    f = float(input('dame la fuerza ?'))
    m = float(input('dame la masa ?'))
    a = f / m
    print(f'\n La aceleracion es {a}')
else:
     print('\nElegiste una opcion valida')
print('Programa terminado')
