# numeros del 1 al 200 de 10 en 10 usando while y continue

c=1
while c <=200:
    c+=1
    if c%10!=0:
        continue
    print (c,end='')
