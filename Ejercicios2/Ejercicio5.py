"""
Caso. Una organización utiliza una escala didáctica de salarios expresados en unidades monetarias.
Ingrese un salario no negativo. Aplique 20 % hasta 9000 inclusive, 10 % para más de 9000 y hasta 15000,
5 % para más de 15000 y hasta 20000, y 3 % para más de 20000. El porcentaje se aplica al salario
completo.
Muestre porcentaje, aumento y nuevo salario.

Fórmula o relación: Aumento = salario × porcentaje / 100. Nuevo salario = salario + aumento.

ENTRADA:

salario = Salario indicado por el usuario

PROCESO:

salario_final = if salario <= 9000 + 20%
                    salario = salario + 20%
                elif salario <= 15000 + 10%
                    salario = salario + 10%
                elif salario <= 20000 + 5%
                    salario = salario + 5%
                else:
                salario >= 20001 + 3%
                    salario = salario + 3%


SALIDA:

salario con porcentaje aplicado

"""

salario = int(input("Cuanto es tu salario?; "))
porcentaje = int()

if salario <= 9000:
    porcentaje = 20/100
    porcentaje_texto = "20%"
elif salario <= 15000:
    porcentaje = 10/100
    porcentaje_texto = "10%"
elif salario <= 20000:
    porcentaje = 5/100
    porcentaje_texto = "5%"
elif salario >= 20001:
    porcentaje = 3/100
    porcentaje_texto = "3%"

aumento = (salario * porcentaje)
salario_total = (salario * porcentaje) + salario

print("Tu porcentaje correspondiente es el ", porcentaje_texto, " tu aumento es: $", aumento, "tu nuevo salario es: $",salario_total)