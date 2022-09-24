##


maximum = int(input(" Porfavor introduce el numero maximo : "))
Oddtotal = 0
number = 1
 
while number <= maximum:
    if(number % 2 == 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number
    number = number + 1

print("La suma de todos los numeros de  1 a {0} = {1}".format(maximum, Oddtotal)) 
