# Calcular la suma y el promedio de 3 calificaciones

print('Calculando la suma y el promedio de 3 calificaciones\n')
#c1 = int(input('Dame calificacion 1?'))
#c2 = int(input('Dame calificacion 2?'))
#c3 = int(input('Dame calificacion 3?'))

print('Dame 3 calificaciones separadas por espacios:')
c1,c2,c3 = input().split()
c1,c2,c3 = [int(c1), int(c2),int(c3)]
# prom = (c1+c2+c3)/3
suma = c1+c2+c3
prom = suma/3

print(f'Los numeros fueron : {c1},{c2},{c3} ')
print (f'La suma {suma}')
print (f' El promedio {prom}')