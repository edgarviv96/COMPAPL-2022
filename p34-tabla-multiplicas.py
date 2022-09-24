# Imprime la tabla de multiplicar deseada del 1 al 10
import os
print('Imprime la tabla de mulplcar deseada del 1 al 10 \n')
while(True):
    os.system('clear') # Borrar pantalla , usar cls en windows
    t = int(input('Que tabla quieres? '))
    c = 1
    while(c<=10):
        print(f'{t} x {c} = {t*c}')
    c+=1
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
print('\nGracias por utilizar este programa...')