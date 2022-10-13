# Contar las vocales y consonantes en una fras
print('Contar las vocales y consonantes en una frase\n')
frase = input('Dame una frase ? ')
voc=cons=otro=0
print(frase)
print(f'La frase tiene {len(frase)} caracteres')
for c in frase:
    if c.isalpha():
        if c in 'aeiou':
            voc += 1
        else:
            cons += 1
    else:
        otro+=1
print('Vocales = ', voc)
print('Consonantes = ', cons)
print('Otros = ', otro)