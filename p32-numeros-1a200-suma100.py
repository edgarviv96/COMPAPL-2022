# numeros de 1 a 200, suma 100
print('Generar n numeros para obtener ganancia')
ganar= int(input('Cuanto quieres ganar?'))
c=0
suma=0 
while c<200:
    c+=1
    suma+=c
    print(c,end='')
    if suma>=ganar:
        print('\n')
        break
print ('Suma>', suma)    