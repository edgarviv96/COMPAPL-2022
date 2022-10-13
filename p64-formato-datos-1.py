# Cadenas de formato
import os
os.system('clear')
a = 'Zacatecas'
b = 'Guadalupe'
c = 'Fresnillo'
print('\nArgumentos por posición:\n')
print('Posición numerada con orden : {0} {1} {2} '.format(a, b, c))
print('Posición sin numero : {} {} {} '.format(a, b, c))
print('Posición numerada sin orden : {2} {1} {0} '.format(a, b, c))
print('Posición repetida : {2} {0} {2} '.format(a, b, c))
print('\nArgumentos por nombre: {c1} {c2} {c3}'.format(c2='Jerez',c3='Guadalupe', c1='Rio Grande'))
txt = 'Universidad Autónoma de Zacatecas'
print('\nAlinear el texto y especificar longitud:\n')
print('-{0:<50}-'.format(txt))
print('-{0:>50}-'.format(txt))
print('-{0:^50}-'.format(txt))
print('-{0:*^50}-'.format(txt))
num = 1235
print('\nFormateo de enteros: \n')
print('Decimal : {0:d}'.format(num))
print('Hexadecimal : {0:x}'.format(num))
print('Octal : {0:o}'.format(num))
print('Binario : {0:b}'.format(num))
num = 123.4567
desc = .20
print('\nFormateo de números: \n')
print('Con dos decimales: {0:.2f}'.format(num))
print('Relleno : {0:15.2f}'.format(num))
print('Exponencial : {0:e}'.format(num))
print('Porciento con dec: {0:.2%}'.format(desc))