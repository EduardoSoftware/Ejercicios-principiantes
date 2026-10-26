"""
Entrada:

medida             = Medida dada por le usuario
lim_inferior       = Limite inferior establecido
lim_superior       = Limite superior establecido

Proceso:

resultado_logico    = (verdadero >= limite inferior) Y (falso <= limite superior)

Salida:

resultado_logico    = dentro o fuera del limite

"""

medida = float(input("Ingresa la medida: "))
lim_inferior = float(input("Limite inferior: "))
lim_superior = float(input("Limite supeior: "))

resultado_logico = (medida >= lim_inferior) and (medida <= lim_superior)

print("Resultado es: ", resultado_logico)


