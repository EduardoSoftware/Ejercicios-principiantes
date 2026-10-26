
numero_ciclistas = int(input("Ingrese la cantidad de ciclistas: "))

menor_tiempo = 999999.0
ganador = 0

for _ in range(numero_ciclistas):
    identificador = int(input("Ingrese el identificador: "))
    minutos = int(input("Ingrese los minutos: "))
    segundos = int(input("Ingrese los segundos: "))
    centesimas = int(input("Ingrese las centésimas: "))
    
    tiempo_total = 60 * minutos + segundos + centesimas / 100
    
    velocidad = 900 / tiempo_total

    print("Ciclista", identificador, ":", velocidad, "km/h")

    if tiempo_total < menor_tiempo:
        menor_tiempo = tiempo_total
        ganador = identificador

print("Ganador:", ganador)