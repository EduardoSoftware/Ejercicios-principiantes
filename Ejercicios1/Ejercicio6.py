"""
ENTRADA:

precio_unidad   = Valor del producto
docenas         = Numero de docenas compradas

PROCESO:

precio_final    = Valor del producto por numero de docenas

SALIDA:

precio_final    = Valor a pagar

"""

precio_unidad = int(input("Precio de la unidad: "))
docenas = int(input("Cantidad de docenas compradas: "))
docenas = docenas * 12

precio_final = precio_unidad * docenas

print("El valor a pagar es: $", precio_final)
