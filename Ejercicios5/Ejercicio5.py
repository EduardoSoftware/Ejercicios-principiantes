
def subtotal_descontado(base, descuento):
    subtotal = base * (1 - descuento / 100)
    return subtotal

def total_con_impuesto(subtotal, impuesto):
    total = subtotal * (1 + impuesto / 100)
    return total

base = float(input("Base?: "))
descuento = float(input("Descuento (%): "))
impuesto = float(input("Impuesto (%): "))

subtotal = subtotal_descontado(base, descuento)
total = total_con_impuesto(subtotal, impuesto)

print("Subtotal:", subtotal, "; total:", total, "pesos")