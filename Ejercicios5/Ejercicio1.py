##Area triangulo

def triangulo(num1, num2):
    area_total = (num1 * num2) // 2
    return area_total



base = int(input("Base?: "))
altura = int(input("Altura?: "))
print("\n")
base_dos = int(input("Segunda base?: "))
altura_dos = int(input("Segunda Altura?: "))

area_uno = triangulo(base, altura)
area_dos = triangulo(base_dos, altura_dos)
suma_areas = area_uno + area_dos



print("Areas: ", base, "y", area_dos, "cm²;suma:", suma_areas, "cm²")



