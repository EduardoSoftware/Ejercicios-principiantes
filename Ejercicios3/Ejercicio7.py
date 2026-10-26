

empleados = int(input("Ingrese la cantidad de empleados: "))


total_nomina = 0.0

mayor_sueldo = -1.0
id_mayor = 0

menor_sueldo = 999999.0
id_menor = 0


for _ in range(empleados):
    identificador = int(input("Ingrese el identificador: "))
    edad = int(input("Ingrese la edad: "))
    antiguedad = int(input("Ingrese la antigüedad: "))
    
    suma_antiguedad = 0
    for i in range(1, antiguedad + 1):
        suma_antiguedad += i
    
    sueldo = (100 + edad + suma_antiguedad) / antiguedad
    
    total_nomina += sueldo
    
    print("Empleado", identificador, ":", sueldo)
    
    if sueldo > mayor_sueldo:
        mayor_sueldo = sueldo
        id_mayor = identificador
        
    if sueldo < menor_sueldo:
        menor_sueldo = sueldo
        id_menor = identificador

print("Nómina:", total_nomina)
print("Mayor:", id_mayor)
print("Menor:", id_menor)