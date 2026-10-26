


a = int(input("Dime el numero A: "))
b = int(input("Dime el numero B mayor que A: "))

while a >= b:
    print("El numero B es menor que A, ingresa nuevamente los datos...")

    a = int(input("Dime el numero A: "))
    b = int(input("Dime el numero B mayor que A: "))
    break

i = a + 1

if i == b:
    print("No hay enteros interiores.")

while i < b:
    print(i)
    i += 1