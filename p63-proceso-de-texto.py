# Procesar texto
import os
txt = '''Aprender a programar en python es una tarea \
que requiere tiempo y constancia, la practica \
es lo que da la experiencia'''
os.system('clear')
print(f'Texto:\n{txt}\n')
pal = input('Dame una palabra ? ')
pos = txt.find(pal)
if pos!= -1:
    if txt.startswith(pal):
        print(f'\n{pal}: es la primer palabra del Texto')
    elif txt.endswith(pal):
        print(f'\n{pal}: es la ultima palabra del Texto')
    else:
        print(f'\n{pal}: aparece la primera vez en la posición: {pos} del Texto')
        print(f'\n{pal}: aparece {txt.count(pal)} veces en el Texto')
        txt2 = txt.replace(pal,'#')
        print(f'\nTexto Modificada: {txt2}\n')
else:
    print(f'{pal} no se encuentra en el Texto')
print('\nProcesamiento de la Texto:')
print(f'\nMayusculas: \n {txt.upper()}')
print(f'\nMinusculas: \n {txt.lower()}')
print(f'\nTitulo : \n {txt.title()}')
txt3 = txt.split()
print(f'\nSeparar : \n {txt3}')
print(f'\nUnir : \n {"-".join(txt3)}')