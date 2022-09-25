# Imprme cuadro de asteriscos
print('Imprime cuadro de asteriscos \n')
n = int(input('Que dimensión (n x n)? '))
for i in range(1,n+1):
 for j in range(1,n+1):
  print('*', end='')
 print('\r')