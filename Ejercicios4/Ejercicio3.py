


suma = 0
cantidad = 0

nota = int(input("Nota?"))

while nota != -99:
    suma += nota
    cantidad += 1
    nota = int(input("Nota?"))

if cantidad > 0:
    promedio = suma / cantidad
    print("Cantidad:", cantidad, ";promedio:", promedio)
elif cantidad == 0:
    print("Cantidad:", cantidad, "; Sin notas")














