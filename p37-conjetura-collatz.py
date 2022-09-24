# Conjetura de collatz
print('Imprime la conjetura de collatz')
num = int(input('Dame un número = '))
while num > 1:
 print(f'Número actual {num}')
 if num % 2 == 0:
  num = num // 2
else:
  num = num * 3 + 1
print(f'Número actual {num}')