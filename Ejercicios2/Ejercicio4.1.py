"""
En una institución se cobra cada crédito a un precio informado por el usuario. Ingrese un código
numérico de estudiante, el precio positivo por crédito y la cantidad entera positiva de créditos. Al valor
de los créditos se suma un recargo fijo de 21000 pesos con 1 o 2 créditos, de 42000 pesos con 3 a 5 y
de 63000 pesos con más de 5. Muestre código y pago total.
Fórmula o relación: Base = precio por crédito × créditos. Pago = base + recargo.


ENTRADA:

valor_credito = valor del credito informado por el usuario
codigo_estudiante = Codigo del estudiante
cantidad_creditos = cantidad de creditos
cargo_fijo = 21000 si =< 1; 42000 si =< 3; 63000 si =< 5;


PROCESO:

Calcular el valor de la cantidad de creditos y mostrarlo en pantalla con su codigo correspondiente

SALIDA:

Mostrar el codigo del usuario con su respectivo valor de los creditos y la cantidad de creditos correspondientes

"""

codigo_usuario = input("Indicame el codigo del usuario: ")
valor_credito = int(input("Cuanto cuesta cada credito?: "))
cantidad_creditos = int(input("Cual es la cantidad de creditos?: "))

base_creditos = valor_credito * cantidad_creditos

if cantidad_creditos <= 2:
    recargo = 21000
elif cantidad_creditos <=5:
    recargo = 42000
else:
    recargo = 63000

pago_total = base_creditos + recargo

print("Codigo: ", codigo_usuario, "pago: ", pago_total)



