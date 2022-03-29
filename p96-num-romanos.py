#Cree un diccionario con los números romanos en arábigo y romano:
#1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
# I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, XIX, XX
#Luego se le pide al usuaro un número en arabgo y se imprime su correspondiente número romano, usando los
#valores previamente almacenados en el diccionario

nums = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',11:'XI',12:'XII',13:'XIII',14:'XIV',15:'XV',16:'XVI',17:'XVII',18:'XVIII',19:'XIX',20:'XX'}

n = nums[int(input('Dame el numero de arabigo a convertir a romano '))]
print(f'El numero transformado en romano es: {n}')