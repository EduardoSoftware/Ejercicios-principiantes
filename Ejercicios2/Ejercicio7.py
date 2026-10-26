"""
ENTRADA:

horas_trabajadas = catidad de horas trabajadas en la semana
tarifa_por_hora = pago por hora normal

PROCESO:

Calcular el sueldo bruto: 
Si trabaja hasta 35 horas:
    bruto = horas * tarifa
Si trabaja más de 35 horas: las primeras 35 horas se pagan normal y las extras al $1.5 (bruto = 35 * tarifa + (horas - 35) * 1.5 * tarifa)

Calcular el impuesto progresivo:
si el bruto es de hasta 2000: impuesto = 0
si el bruto esta entre 2000 y 2220: impuesto = (bruto-2000) * 0.20
si el bruto es mayor a 2220: los primero 220 gravables pagan 44 de impuesto (220*0.20 = 44) mas el 30% del excedente (impuesto = 44 + (bruto-2220) * 30)

SALIDA:

Mostrar el sueldo bruto, impuesto y sueldo neto

"""

horas_trabajadas = float(input("Ingrese las horas semanales: "))
tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))

if horas_trabajadas <= 35:
    sueldo_bruto = horas_trabajadas * tarifa_por_hora
else:
    horas_extras = horas_trabajadas - 35
    sueldo_bruto = (35 * tarifa_por_hora) + (horas_extras * 1.5 * tarifa_por_hora)

if sueldo_bruto <= 2000:
    impuesto = 0.0
elif sueldo_bruto <= 2220:
    impuesto = (sueldo_bruto - 2000) * 0.20
else:
    impuesto = 44 + (sueldo_bruto - 2220) * 0.30

sueldo_neto = sueldo_bruto - impuesto

print("Bruto:", int(sueldo_bruto), "; impuesto:", int(impuesto), "; neto:", int(sueldo_neto))