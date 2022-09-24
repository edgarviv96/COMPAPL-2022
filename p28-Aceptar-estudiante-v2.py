# Ceptar estudiante v2
#Dado el nombre del estudiante, sexo (h/m), su edad y tres calificaciones, decidir si el estudiante es aceptado. La 
#Universidad Kitty Kat SA es solo para mujeres mayores de 21 años con un promedio de entre 8 y 9.5


from ast import Return


name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if gender == "M":
        print ('Bienvenida eres aceptada')
    #if name.lower() < "m":
        #group = "A"
else:
       # gender != "M"
        
#else:
   # if name.lower() == "M":
       # group = "A"
    #else:
       # group = "B"
 print ("Solo es para mujeres lo sentimos")
    


        
edad = int (input('Dame tu edad: '))

if edad >= 21:
    print ("Dame 2 calificaciones: \n")
    c1, c2= int (input()), int(input())
    if c1>=8 and c2<=9.5:
     print(f'{name} bienvenido a la Universidad Kitty Kat SA, tu edad es {edad} y tus calificaciones son {c1}, {c2}')
    else: 
     print ('No aceptamos calficaciones menos a 8, lo sentimos')
else: 
 print('No aceptamos menores de edad, lo sentimos')