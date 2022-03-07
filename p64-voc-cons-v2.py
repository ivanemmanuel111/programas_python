#Modifique el programa p59 - vocales, consonantes
# para que además de contar cuantas vocales y consonantes tiene una frase, imprima cuales son estas. (ver también p61)
#Frase ? El dia se pasa muy rapido
#Vocales 10 - Eiaeaauaio
#Consonantes 10 - ldspsmyrpd

frase = str.lower(input('dame una frase: '))
voc = cons = 0
print(frase)
print (f'La frase tiene  {len(frase)} caracteres ')
print('Las vocales son: ')
for v in frase:
    if v.isalpha():
       if v in 'aeiou':
           voc+= 1
           
           print(v,end='') 
print('')    
print('Las consonates son: ')      
for c in frase:
    if c.isalpha():
       if c in 'bcdfghjklmnñpqrstvwxyz':
           cons+= 1
           print(c,end='')
print(f'\nVocales = {voc} ')
print(f'\nConsonantes = {cons} ')