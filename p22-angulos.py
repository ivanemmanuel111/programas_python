# Muestra el tipo de angulos segun su tamaño
# <90 agudo

print('Mostrando el tipo de angulo segun su tamaño ...')
angulo = int(input('Dame el angulo ?'))
print(f'El angulo es de {angulo} por lo tanto es un angulo: ', end = '')
if angulo < 90 :
      print('agudo')
elif angulo == 90 :
      print('recto')
elif angulo > 90 and angulo < 180 :
      print('obtuso')
elif angulo == 180 :
      print('llano')
elif angulo > 180 and angulo < 360 :
      print('concavo')
else:
    print('angulo fuera de rango')