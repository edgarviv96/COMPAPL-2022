# Dividir en palabras y contar
import os
os.system('clear')
print('Dividir en palabras y contar: \n')
frase = '''Al año los murcielagos huyen de la fuerte \
luz que baja por el kiosko de wivex'''
print(f'La frase: \n{len(frase)} - {frase}\n')
palabras = frase.split()
print(f'Lista de palabras : \n{palabras}\n')
print(f'{"Division de palabras":-^50}')
for palabra in palabras:
    print(f'{len(palabra):>4} - {palabra:<12}', end=' ')
v=c=0
for car in palabra:
    if car.isalpha():
        if car.lower() in 'aeiou': v+=1
        else: c+=1
    print(f'v:{v:>3} c:{c:>3}')
print(f'{"final":-^50}')