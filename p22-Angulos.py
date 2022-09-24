# Muestra al tipo de angulo
# <90 agudo, =90 recto, >90 y <180 obtuso, =180 llano, >180 y <360 concavo

print('Mostrando el tipo de angulo en base a los grados')

angulo = int(input('Dame un angulo ?'))
print(f'El angulo tiene {angulo} grados por lo tanto es: ',end='')

if angulo>=0 and angulo>=360 :
    if angulo < 90 :
        print('Agudo')
    elif angulo==90:
        print('Recto')
    elif angulo > 90 and angulo<180:
        print('obtuso')
    elif angulo ==180:
        print('llano')
    elif angulo >180 and angulo <360:
        print ('concavo')
else:
    print(f'El angulo {angulo} esta fuera de rango')