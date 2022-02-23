#Se desea calcular el promedio de 5 calificaciones introducidas por el usuario
# luego evaluar el resultado e imprimir un mensaje de acuerdo al promedio obtenido:
# Entre 0 y 6 Quedas reprobado
# Entre 6.1 a 7 Pasas de panzazo
# Entre 7.1 y 8 Muy bien, pues mejorar
# Entre 8.1 y 9 Excelente sigue así
# Entre 9.1 y 10 Perfecto tu esfuerzo valió la pena

print('Dame 5 calificaciones: ')
c1, c2, c3, c4, c5 = input().split()
c1, c2, c3, c4, c5 = [float(c1), float(c2), float(c3), float(c4), float(c5)]
ev = (c1 + c2 + c3 + c4 + c5) / 5
if ev <= 6:
    print(f' Promedio {ev}, quedas reprobado')
elif ev > 6 and ev <= 7:
    print(f' Promedio {ev}, pasas de panzazo')
elif ev > 7 and ev <= 8:
    print(f' Promedio {ev}, Muy bien, pues mejorar')
elif ev > 8 and ev <= 9:
    print(f' Promedio {ev}, Excelente, sigue así')
elif ev > 9 and ev <= 10:
    print(f' Promedio {ev}, Perfecto, tu esfuerzo valió la pena')
else :
    print('.....Error....')