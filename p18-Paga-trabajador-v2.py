#Calcular la paga total de un trabajador v2

from tracemalloc import take_snapshot


print ('Calculando la paga de un trabajador \n\n')

#Entrada
nombre= input ('Dame el nombre')
horas= int(input('Dame las horas trabajdas'))
paga= float (input('Dame paga por hora'))
tasa= 0.3

#calculo

if horas <= 40:
    pagabruta = horas * paga
else: 
    extra = horas -40
    pagabruta= (horas * paga) + (extra * paga * 2)



impuesto= pagabruta * tasa
paganeta= pagabruta - impuesto

#Salida

print ('\n Resumen de pagas \n')
print (f'El trabajador {nombre}, trabajo {horas}, con una paga de {paga} pesos la hora \n')
print (f'Paga bruta = {pagabruta}')
print (f'Impuesto = {impuesto}')
print (f'Paga neta = {paganeta}')