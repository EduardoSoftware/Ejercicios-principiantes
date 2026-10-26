
capital = float(input("Ingrese el capital inicial: "))
interes = float(input("Ingrese la tasa anual porcentual: "))
anios = int(input("Ingrese la cantidad de años: "))

saldo = capital

# Ciclo for para calcular el saldo año tras año durante catidad años
for _ in range(anios):
    saldo = saldo * (1 + interes / 100)

print("Saldo:", saldo)
