# Segunda Ley de Newton

print('[F]          f= m * a')
print('[M]          m= f / a')
print('[A]          a= f / m')

op= str.upper(input('Elige una opcion'))

if op== 'F':
    print('\n Calculando la Fuerza')
    m= int(input('Dame la masa'))
    a= int(input ('Dame la aceleración'))
    f= m*a
    print (f'La fuerza es {f}')

if op== 'M':
    print('\n Calculando la Masa')
    m= int(input('Dame la fuerza'))
    a= int(input ('Dame la aceleración'))
    f= m/a
    print (f'La masa es {m}')

if op== 'A':
    print('\n Calculando la Aceleración')
    m= int(input('Dame la fuerza'))
    a= int(input ('Dame la masa'))
    f= f/m
    print (f'La aceleración es {a}')
else:
    print ('Opcion invalida')

print('\n Gracias por utilizar este programa')