# Calificación con letra

def califletra(cal):
    letra = ''
    msj = ''
    if cal>=90 and cal<=100:
       letra = 'A'
       msj = 'Excelente'
    elif cal>=80 and cal<90:
       letra = 'B'
       msj = 'Bien'
    elif cal>=70 and cal<=80:
       letra = 'C'
       msj = 'Suficiente'
    elif cal>=60 and cal<70:
        letra = 'D'
        msj = 'Deficiente'
    elif cal>=0 and cal<60:
        letra = 'F'
        msj = 'Reprobado'

    return letra, msj #Asi nos ahorramos los returns de los ifs

calificacion = int(input('Dame una calificacion entre 1 y 100? '))
letra, msj= califletra(calificacion)
print(f'Tu calificacion de {calificacion} corresponde a {letra} y el mensaje es {msj}')