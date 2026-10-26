"""
ENTRADA:

precio_original     = Valor del articulo
porcentaje          = Porcentaje de descuento

PROCESO:

discount            = valor del descuento
final_price         = precio_original - discount

SALIDA:

precio_original     = valor original - descuento

"""

precio_original = float(input("Precio del articulo: "))
porcentaje = int(input("Porcentaje de descuento: "))

discount = precio_original * (porcentaje / 100)

final_price = precio_original - discount

print("Precio del producto: $", precio_original, ", menos el descuento de: $", discount, ", el total seria: $", final_price)
