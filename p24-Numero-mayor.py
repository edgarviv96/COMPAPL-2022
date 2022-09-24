#Dados tres números enteros, verificar cual es el mayor.
lista = [2,6,8,10,5154,5,8,8,8]

Menor= None
Mayor = None

for numero in lista:
    if Menor==None and Mayor==None:
        Menor=numero
        Mayor=numero
    else: 
        if numero<Menor:
            menor=numero
        if numero>Mayor:
            Mayor=numero
print (f'El numero mayor es' , (Mayor))
#print(f'El numero menor es', (Menor))

    