# Agregar elementos a la lista

nums = [80.3, 12.5, 60.2, 30.4]
print(f'Todos los números : {nums}')

nums.append(90); nums.append(100) #Agregar dos numero al final
print(f'Agregar 90 y 100 al final de la lista : {nums}')

nums.insert(4,80) #Insertar un 90 en pos 4 y recorre lo demas
print(f'Insertar 80 en [4] : {nums}')

otros = [110,120,130] #Agregar estos numeros
nums.extend(otros) #A partir del ultimo digito
print(f'Extender con 110,120,130 : {nums}')

n = int(input('Numero: ')) #pide el numero a agregar
nums.append(n)  #agregar numero
print(nums)
