
def valor_absoluto(numero):
    if numero < 0:
        return -numero
    return numero

def es_aceptable(medicion, objetivo, tolerancia):
    diferencia = medicion - objetivo
    error = valor_absoluto(diferencia)
    return error <= tolerancia

objetivo = float(input("Objetivo?: "))
tolerancia = float(input("Tolerancia?: "))
print("\n")
medicion_uno = float(input("Primera medicion?: "))
medicion_dos = float(input("Segunda medicion?: "))

aceptable_uno = es_aceptable(medicion_uno, objetivo, tolerancia)
aceptable_dos = es_aceptable(medicion_dos, objetivo, tolerancia)

print("Aceptables:", aceptable_uno, ";", aceptable_dos)