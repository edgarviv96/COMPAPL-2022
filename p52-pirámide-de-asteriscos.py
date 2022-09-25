# Imprime pirámide de asteriscos
print('Imprime pirámide de asteriscos \n')
n = int(input('Cuantos renglones ? '))
for i in range(1,n+1):
 for j in range(1,i+1):
   print('*', end='')
 print('\r')