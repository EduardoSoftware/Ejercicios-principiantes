
def precio_unitario(precio_total, cantidad_gramos):
    precio_gramo = precio_total / cantidad_gramos
    return precio_gramo

precio_1 = float(input("Precio paquete 1?: "))
gramos_1 = float(input("Gramos paquete 1?: "))
print("\n")
precio_2 = float(input("Precio paquete 2?: "))
gramos_2 = float(input("Gramos paquete 2?: "))

p_gramo_1 = precio_unitario(precio_1, gramos_1)
p_gramo_2 = precio_unitario(precio_2, gramos_2)

print("Precios por gramo:", p_gramo_1, "y", p_gramo_2, "pesos")


if p_gramo_1 < p_gramo_2:
    print("conviene paquete 1")
elif p_gramo_2 < p_gramo_1:
    print("conviene paquete 2")
else:
    print("igualdad")