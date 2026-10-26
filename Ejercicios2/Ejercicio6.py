"""
Liquidar una llamada internacional
Caso:
Un ejercicio de facturación utiliza cinco destinos: 1 Estados Unidos con tarifa de 0,65 dólares por minuto y sobretasa de 0 %; 2 Canadá con 0,82 y 2,5 %; 3 México con 0,50 y 2,1 %; 4 Chile con 0,91 y 2,2%; 5 España con 1,01 y 2,9 %. Ingrese el código, los minutos no negativos y la tasa positiva de cambio en pesos por dólar. Para un código desconocido informe «Destino inválido»; en otro caso muestre el costo en pesos.

Fórmula o relación: Costo en pesos = minutos × tarifa por minuto × (1 + sobretasa / 100) × tasa de cambio.

ENTRADA:

destino = codigo del destino (del 1 al 5)
minutos = Tiempo en llamada
Tasa_cambio = cuantos pesos cuesta el dolar

PROCESO:

Buscar la tarifa y la sobretasa según el código del destino elegido:
Si es 1: Tarifa = $0.65$ y Sobretasa = $0$
Si es 2: Tarifa = $0.82$ y Sobretasa = $2.5$
Si es 3: Tarifa = $0.50$ y Sobretasa = $2.1$
Si es 4: Tarifa = $0.91$ y Sobretasa = $2.2$
Si es 5: Tarifa = $1.01$ y Sobretasa = $2.9$
Si es otro número: El destino no es válido.

SALIDA:

Mostar el costo total en pesos
si el codigo no esta entre 1 y 5 mostrar el mensaje "Destino no invalido"

"""

codigo_destino = int(input("Ingrese el código del destino (1-5): "))
minutos = float(input("Ingrese los minutos (no negativos): "))
tasa_cambio = float(input("Ingrese la tasa de cambio en pesos por dólar: "))

if codigo_destino == 1:
    tarifa_por_minuto = 0.65
    sobretasa = 0.0
elif codigo_destino == 2:
    tarifa_por_minuto = 0.82
    sobretasa = 2.5
elif codigo_destino == 3:
    tarifa_por_minuto = 0.50
    sobretasa = 2.1
elif codigo_destino == 4:
    tarifa_por_minuto = 0.91
    sobretasa = 2.2
elif codigo_destino == 5:
    tarifa_por_minuto = 1.01
    sobretasa = 2.9
else:
    tarifa_por_minuto = None


if tarifa_por_minuto is None:
    print("Destino inválido")
else:
    costo_pesos = minutos * tarifa_por_minuto * (1 + sobretasa / 100) * tasa_cambio
    
print("Costo: ", costo_pesos, "pesos")