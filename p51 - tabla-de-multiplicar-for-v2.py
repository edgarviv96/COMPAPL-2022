# Imprime las tablas de la tabla 1 a la tabla n
import os
print('Imprime las tablas de la tabla 1 a la tabla n')
os.system('clear')
n = int(input('Hasta que tabla quieres ? '))
m = int(input('Hasta donde la deseas ? '))
for i in range(1,n+1):
 for j in range(1,m+1):
  print(f'{i} x {j} = {i*i}')
 print('\n')