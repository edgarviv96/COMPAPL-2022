# Acceder a los elementos de una lista
import os; os.system('clear')
nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]
print('Acceder a los elementos de una lista\n')
print(f'Cuantos números son : {len(nums)} \n')
print(f'Todos los números : {nums} \n')
print(f'Primero y último : {nums[0]}, {nums[-1]} \n')
print(f'Del 2 al 6 : {nums[2:6]} \n')
print(f'Los primeros 3 : {nums[:3]} \n')
print(f'Los últimos 3 : {nums[6:]} \n')
print(f'3 antes del último : {nums[-4:-1]} \n')