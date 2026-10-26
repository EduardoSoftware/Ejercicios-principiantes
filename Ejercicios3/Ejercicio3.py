#cantidad de empleados
numero = int(input("Ingrese la cantidad de empleados: "))

#Valor inicial para la nomica en este caso el valor minimo que no afecta es 0
total_nomina = 0

#por variable nomina en un rango (Numero de veces que se repite); 
for nomina in range(numero):
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    total_nomina += sueldo

print("Nomina:", total_nomina)