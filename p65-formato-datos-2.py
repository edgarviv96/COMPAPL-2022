# formateo de datos ejemplo 2
import os; os.system('clear')
noms = 'Juan Carlos Pedro Luis Jose Maria Julian Teresa Francisco Leticia Rafael'
nombres = noms.split()
edad = 25
sueldo = 123.45686
tasa = 0.30
print('Salida datos con f: \n')
print(f'Nombre: {nombres[0]}, Edad: {edad}, Sueldo: {sueldo:.2f} Tasa: {tasa:.2%} \n')
print(f'Los nombres: \n\n{nombres}\n')
print(f"{'Tabla de datos':^45}")
print('-'*45)
print(f"{'Nombre':<15}{'Edad':^15}{'Sueldo':>15}")
print('-'*45)
for i in range(len(nombres)):
    print(f'{nombres[i]:<15}{edad+i:^15}{sueldo*i:>15,.2f}')
print('-'*45)