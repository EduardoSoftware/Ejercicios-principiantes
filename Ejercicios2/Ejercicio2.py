"""
ENTRADA:

edad = edad de la persona en anios cumplidos, no numero negativo

PROCESO:

si el usuario tiene mas de 18 anios, mayor de edad
sino menor de edad

SALIDA:

mayor o menor de edad, si cumple o no la condicion +18

"""

edad = int(input("Ingresa tu edad: "))

if edad > 18:
    print("Mayor de edad")
elif edad < 18:
    print("Menor de edad")