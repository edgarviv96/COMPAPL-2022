#Volumen de cilindro

from xml.etree.ElementTree import PI

import math

print ('Calcular el volumen de un cilindro')
radio, altura = int(input(f'Radio: ''\n')), int(input(f'Altura: ''\n'))

#radio = input('Dame el radio: ') # lee cadena
##altura = int(input('Dame la altura: ')) 

Volumen= (math.pi*(radio * radio))* (altura) 

print (f'El volumen del cilindro es: {Volumen}''\n')