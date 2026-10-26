capital = float(input("Capital inicial: "))
interes = float(input("Tasa de interes (%): "))
anios = int(input("Cantidad de años: "))

while capital < 0 or interes <= 0 or interes >= 100 or anios <= 0:
    print("Datos invalidos, intente otra vez")

    capital = float(input("Capital inicial: "))
    interes = float(input("Tasa de interes (%): "))
    anios = int(input("Cantidad de años: "))

saldo = capital
anio = 1

while anio <= anios:
    saldo = saldo + (saldo * interes / 100)

    print("Saldo del año", anio, ":", round(saldo, 2))

    anio = anio + 1

print("Saldo final:", round(saldo, 2))