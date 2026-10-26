
def pago_semanal(horas, tarifa):
    if horas <= 40:
        pago = horas * tarifa
    else:
        pago = (40 * tarifa) + ((horas - 40) * tarifa * 1.5)
    return pago

print("--- Persona 1 ---")
horas_1 = float(input("Horas semanales persona 1?: "))
tarifa_1 = float(input("Tarifa por hora persona 1?: "))

print("\n--- Persona 2 ---")
horas_2 = float(input("Horas semanales persona 2?: "))
tarifa_2 = float(input("Tarifa por hora persona 2?: "))

pago_uno = pago_semanal(horas_1, tarifa_1)
pago_dos = pago_semanal(horas_2, tarifa_2)
total_pagos = pago_uno + pago_dos

print("Pagos:", pago_uno, "y", pago_dos, "pesos; total:", total_pagos)