# Se desea calcular la hipotenusa de un triángulo rectángulo dadas las longitudes de sus lados
# hipotenusa = raizcuadrada( longlado1 * longlado1 + longlado2 * longlado2 )

from cmath import sqrt
import math

longlado1 = float(input('Escriba el valor de longitud lado 1: '))
longlado2 = float(input('Escriba el valor de longitud lado 2: '))

hipotenusa = math.sqrt(longlado1 * longlado1 + longlado2 * longlado2)
print(f'La hipotenusa es: {hipotenusa}')