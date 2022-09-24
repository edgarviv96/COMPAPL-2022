#Convertir de farnheit a centigrados y viceversa

print ('Convertir de farenheit a centigrados y viceversa\n')
print ('[C] Convertir a centigrados')
print ('[F] Convertir a farenheit')
opcion = str.upper (input('Elige'))

if opcion == 'C':
    print('\n Elegiste convertir a centigrados\n')
    temp= float (input ('Dame los grados farenheit'))
    res= (temp -32)* 5/9
    print (f'{temp} grados farenheit, equivale a {res:.2f} grados centigrados')

else:
   print('\n Elegiste convertir a farenheit\n')
   temp = float (input ('Dame los grados centigrados'))
   res= (temp * 9/5)+ 32
   print (f'{temp} grados centigraops, equivale a {res:.2f} grados farenheit')