# Dados dos ángulos de un triángulo, calcular el 3er ángulo, usando la siguiente formula:
# angulo3 = 180 – (angulo1 + angulo2)

angulo1 = float(input('Valor angulo 1: '))
angulo2 = float(input('Valor angulo 2: '))

angulo3 = 180 - (angulo1 + angulo2)

print(f'El valor del angulo3 es {angulo3}')
