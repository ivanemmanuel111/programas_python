#Modifique el programa p60 - contar letras, dígitos, símbolos
# para que además de contar cuantas letras, dígitos y símbolos tiene una frase palabra, imprima cuales son estos.
#  (ver también p61)
#Frase ? ¡Los numeros 123#!
#Caracter 10 : Losnumeros
#Digito 3 : 123
#Simbolo 3 : ¡#!

frase = str.lower(input('dame una frase: '))
car = dig = sim = 0
print(frase)
print (f'La frase tiene  {len(frase)} caracteres ')

print('')    
print('Los caracteres: ')  
for c in frase:
    if c.isalpha():
       if c in 'abcdefghijklmnñopqrstuvwxyz':
           car+= 1     
           print(c,end='') 
print('')    
print('Los digitos: ') 
for v in frase:
    if v.isdigit():
       if v in '0123456789':
           dig+= 1
           print(v,end='')
print('')    
print('Los simbolos: ') 
for s in frase:
    if s.find('!"#$%&/()=?¡¿*-+.,_{[}]|°'):
       if s in '!"#$%&/()=?¡¿*-+.,_{[}]|°':
           sim+= 1
           print(s,end='')
print(f'\nCaracteres {car}, \n Digitos {dig}, \nSimbolos {sim} ')