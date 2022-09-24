# convierte numeros enteros a numero romanos

finteger_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def integer_to_roman(integer):
    roman = '' # Se declara la variable roman y se le asigna una cadena vacía.

    while integer > 0: # Mientras el número ingresado sea mayor a cero.
        for i, r in finteger_roman: # Iteramos en la lista integer_roman sobre cada par entero-romano.
            while integer >= i: # Mientras el número sea mayor o igual al iterable i. 95 >= 90 -> roman = XC -> integer = 5
                roman += r # A la variable roman le sumamos lo que vale r.
                integer -= i # A la variable num le sumamos lo que vale r.

    return roman # Regresamos el número romano.

integer = int(input('Ingrese un número entero: '))
print(f'El número ingresado es: {integer_to_roman(integer)}')

