"""
ENTRADA:

num1 = primer numero entero en orden creciente
num2 = segundo numero entero en orden creciente
num3 = tercer numero entero en orden creciente

PROCESO:

determinar si el orden es creciente o no
si num1 < num2
    entonces num2 < num3
    decir "orden estrictamente creciente"
sino
    decir "no esta en orden estrictamente creciente"

SALIDA

determinar si el orden de los numero ingresados por el usuario esta en orden creciente

"""

num1 = int(input("Dime un numero entero en orden creciente: "))
num2 = int(input("Dime un segundo numero en orden creciente: "))
num3 = int(input("Dime un tercer numero en orden creciente: "))

if num1 < num2 and num2 < num3:
    print("Orden estrictamente creciente")
else:
    print("No esta en orden estrictamente creciente")


