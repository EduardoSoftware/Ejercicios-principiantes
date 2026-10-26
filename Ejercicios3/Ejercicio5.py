ventas = int(input("Ingrese la cantidad de ventas (N): "))

# Contadores para cada grupo
grupo1 = 0
grupo2 = 0
grupo3 = 0

# Ciclo for para procesar cada venta
for _ in range(ventas):
    valor_venta = float(input("Ingrese el valor de la venta: "))
    
    if valor_venta <= 200:
        grupo1 += 1
    elif valor_venta < 400:
        grupo2 += 1
    else:
        grupo3 += 1

print("Grupos 1, 2 y 3:", grupo1, ";", grupo2, ";", grupo3)