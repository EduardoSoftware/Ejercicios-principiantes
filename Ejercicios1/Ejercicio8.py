"""
Entrada:

costo       = costo del producto
margen      = margen de ganancia deseado


Proceso:

precio_venta = costo * (100 + margen) / 100

Salida:

precio_venta = valor final del producto 

"""

costo = int(input("Ingresa el costo de producto: $"))
margen = int(input("Margen de ganancia deseado: "))

precio_venta = costo * (100 + margen) / 100

print("El precio de venta es: $", precio_venta)