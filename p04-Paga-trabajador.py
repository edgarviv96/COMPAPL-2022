# Calcular la paga total de un trabajador
print('Calculando la paga de un trabajador')

# Entrada
nombre= input('Dame el nombre?')
horas= int(input('Dame las horas trabajadas?'))
paga= float (input('Dame paga por hora?'))
tasa = 0.3

# Calculo
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

# Salida
print('Resumen de pagos')
print(f'El trabajador {nombre}, trabajo {horas} horas, con una pada de {paga} pesos la hora, se asume un impuesto de {tasa}%')
print(f'Paga bruta {pagabruta}')
print(f'Impuessto {impuesto}')
print(f'Paga neta {paganeta}')