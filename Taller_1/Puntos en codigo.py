# Punto_1
dividendo = int(input("Colocar un numero: "))
divisor = int(input("Colocar otro numero: "))

cociente = dividendo / divisor
residuo = dividendo % divisor

print("El cociente es = ", cociente)
print("El residuo es = ", residuo)


# Punto_2
estatura = float(input("Pon tu estatura en cm, Ej: 1.74: ")) 
peso = float(input("Pon tu peso en Kg: "))

formula = peso / (estatura)**2

print(" Su IMC es", format(formula, ".2f"))


# Punto_3
precio = int(input("Coloque el precio final del producto: "))

IVA = precio * 0.19
Bruto = precio * 1.19

print(precio,"$ Valor del IVA=",IVA,"$ Valor Bruto=", Bruto,"$")


# Punto_4
distancia = int(input("distancia recorrida anual (Km): "))
consumo = int(input("Consumo anual del vehiculo (L): "))
costo = float(input("Costo promedio anual ($): "))

costotal = (distancia*consumo) / 100*costo

print("El costo anual del consumo de combustible = $", costotal)