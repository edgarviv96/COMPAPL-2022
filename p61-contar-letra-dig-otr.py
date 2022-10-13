# Contar letras, digitos, simbolos
print('Contar letras, digitos, simbolos\n')
frase = input('Dame una frase ? ')
let=dig=sim=0
print(frase)
print(f'La frase tiene {len(frase)} caracteres ')
for c in frase:
    if c.isalpha():
        let+=1
    elif c.isdigit():
        dig+=1
    else:
        sim+=1
print(f'\nLetras {let},\nDigitos {dig},\nSimbolos {sim}')