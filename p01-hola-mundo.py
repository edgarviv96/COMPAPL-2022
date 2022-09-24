# Leer datos y enviar saludo

print('Leyendo datos y enviar un saludo')
nombre = input('Dame tu nombre: ') # lee cadena
edad = int(input('Dame la edad: ')) # lee cadena y convierte a entero
peso = float(input('Dame tu peso: ')) # lee una cadena y convierte a float

#print (''Hola', nombre, 'bienvenido a python, tu edad es', edad, 'tu peso es', peso''''''''')
print(f'Hola {nombre} bienvenido a python, tu edad es {edad}, tu peso es {peso}')

print(type(nombre))
print(type(edad))
print(type(peso))  
