#Diseña un programa con dos funciones que convierta: pulgadas a centímetros y metros a pies. Deberá mostrar un
#menú con las opciones correspondientes. ( ver p102 temperaturas)
#Considere las siguientes formulas:
# centímetros = pulgadas * 2.54
# pies = metros * 3.281 

def centimentros(pulgadas):
   return pulgadas * 2.54

def pies(metros):
   return metros * 3.281

print('[ 1 ] Convertir a centimetros')
print('[ 2 ] Convertir a pies')
op = int(input("Elige? "))

if op==1 :
   print('Convertir a centimetros')
   pulgadas = int(input('Dame la medida en pulgadas? '))
   print(f'La medida a centimetros es es {centimentros(pulgadas)}')
elif op==2:
   print('Convertir a pies')
   metros = int(input('Dame la medida en metros? '))
   print(f'La medida en pies es {pies(metros)}')