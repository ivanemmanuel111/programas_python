#import random
from random import randint #importa solo la funcion randint
from os import system 
#de la libreria solo importa la funcion

MAX = 20
def genera_aleatorios():
    nums = []
    for i in range(MAX):
       nums.append(randint(1,100))
    return nums

def suma_listas(num1, num2):
    suma = []
    for i in range(MAX):
       suma.append( nums1[i] + nums2[i] )
    return suma

system('clear')
nums1 = genera_aleatorios()
nums2 = genera_aleatorios()
suma = suma_listas(nums1, nums2)

print(f'Lista 1 : {nums1}')
print(f'Lista 2 : {nums2}')
print(f'Suma listas : {suma}')