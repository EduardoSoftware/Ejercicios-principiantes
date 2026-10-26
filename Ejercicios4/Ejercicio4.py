

trabajadores = 0

salario_mensual = float(input("Salario mensual?: "))

while salario_mensual != 0:
    dias_trabajados = int(input("Dias trabajados?: "))
    bonos = float(input("Bonos?: "))
    otras_deducciones = float(input("Otras deducciones?: "))
    
    salario_proporcional = (salario_mensual * dias_trabajados) / 30
    devengado = salario_proporcional + bonos
    neto = (devengado * 0.83) - otras_deducciones
    
    print("Neto:", neto)
    
    trabajadores += 1
    salario_mensual = float(input("Salario mensual?: "))



if trabajadores == 0:
    print("Sin trabajadores")