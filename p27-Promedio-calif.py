# Calcular el promedio de 5 calificacion

print('Ingresa 5 calificaciones:\n')

cali1 = float(input('Dame la primer calif: '))

cali2 = float(input('Dame la segunda calif: '))

cali3 = float(input('Dame la tercer calif: '))

cali4 = float(input('Dame la cuarta calif: '))

cali5 = float(input('Dame la quinta calif: '))

promedio = (cali1+cali2+cali3+cali4+cali5)/5


if promedio ==10 :
    if promedio >0 and promedio <6 :
     print('Reprobado')

    elif promedio>6.1 and promedio <7:
     print('Pasaste de panzaso')
    elif promedio>7.1 and promedio <8:
     print('Muy bien, Puedes mejorar')
    elif promedio>8.1 and promedio<9:
     print('Excelente sigue así')
    elif promedio>9 and promedio==10 :
     print ('Mejoraste, bien hecho')
#else:
    #print (f'El promedio es:{promedio} ') 