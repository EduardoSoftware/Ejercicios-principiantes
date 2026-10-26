
#Solicitar los datos iniciales numero a, numero d y la cantidad
num_a = int(input("Numero A: "))
num_d = int(input("Numero D: "))
cantidad = int(input("Cantidad: "))

#suma es 0, porque debe tener un valor inicial que es 0, el valor base que no suma ni resta; termino_actual es el valor del primer dato para tener un punto de partida establecido
suma = 0
termino_actual = num_a

#por la cantidad de veces en un rango con dependencia  ala variable cantidad, suma es + o = a termino actual; termino actual es + o = a numerod(El segundo valor) esto hace que cuando el ciclo por se le establece una cantidad de veces (cantidad) se repetira su contenido dependiento de esa cantidad, lo cual hacemos que se repita x veces la sigueite intruccion, suma es mas o igual que termino actual; termino actual es + o = que numd, generando una retroalimentacion que se repite por la cantidad de veces iniciales establecidas
for veces in range(cantidad):
    suma += termino_actual
    termino_actual += num_d

print("Suma:", suma)

