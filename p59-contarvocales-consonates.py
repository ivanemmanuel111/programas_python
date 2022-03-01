# Contar vocales y consonantes

frase = input('dame una frase: ')
voc = cons = 0
print(frase)
print (f'La frase tiene  {len(frase)} caracteres ')
for c in frase:
    if c.isalpha():
       if c in 'aeiou':
           voc+= 1
       else: 
            cons +=1
print(f'Vocales = {voc} ')
print(f'Consonantes = {cons} ')