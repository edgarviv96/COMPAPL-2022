# Uso de las funciones trigonometricas en python
import math

print('Uso de las funciones trigonometricas de python')

angulo = int(input('Dame el angulo en radianes'))
seno = math.sin(angulo)
coseno = math.cos(angulo)
tangente = math.tan(angulo)
grados = math.degrees(angulo)

salida=('Resumen de funciones\n'
f'El seno es {seno:.2}\n'
f'El coseno es {coseno:.2}\n'
f'La tangente es {tangente:.2}\n'
f'El angulo {angulo} en radianes equivale a {grados:.2} grados\n')

print(salida)