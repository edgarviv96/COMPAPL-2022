# Calcular la hipotenusa de un triangulo rectangulo


import math

print ('Dame los numeros de los lado por separado')
lado1, lado2= float (input ()), float (input ())

hipotenusa = math.sqrt( lado1 * lado1 + lado2 * lado2 )
print( f'La hipotenusa es {hipotenusa}') 