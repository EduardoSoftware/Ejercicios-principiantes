"""
ENTRADA:

codigo = codigo del producto asignado por el usuario
existencia = cantidad de unidadaes existentes
cantidad_minima = cantidad minima permitida en stock
pedido_previsto = cantidada prevista para futuro pedido
precio = precio del articulo por unidad

PROCESO:

verificar con el codigo si el producto tiene el stock adecuado, sino, realizar orden de pedido con el costo estimado del producto y sugerir la cantidad de articulos para pedido.

SALIDA:

codigo del producto, requiere o no pedido, costo del pedido

"""

codigo = input("Indicame el codigo del producto: ")
existencia = int(input("Cuantas unidades hay en stock?: "))
cantidad_minima = int(input("Cual es la cantidad minima permitida?: "))
precio = int(input("Cuanto cuesta la unidad?: "))

pedido_previsto = cantidad_minima - existencia
precio_pedido = pedido_previsto * precio

if existencia < cantidad_minima:
    print("Desbes hacer el pedido del producto codigo: ", codigo, " por la cantidad de: ", pedido_previsto, " con un costo de: $", precio_pedido,)
elif existencia > cantidad_minima:
    print("No requiere pedido.")
else:
    print("Datos ingresados no validos")

