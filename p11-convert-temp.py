# Dada una temperatura en grados celcius, obtener su equivalente en grados farenheit, usando la siguiente formula:
# farenheit = (celcius × 9/5) + 32

gradoscelcius = int(input('Dar temperatura en celcius: '))

farenheit = ((gradoscelcius * 9/5) + 32)

print(f'La temperatura en grados farenheit es {farenheit}')