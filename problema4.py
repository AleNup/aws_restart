#Se necesita un programa que calcule el precio final de un producto que cuenta con el 15% de descuento.
#Input: Precio del producto (float > 0)
#Output: Precio total con descuento (float > 0)

precio = float(input("Ingrese el precio: "))

descuento = precio * (15/100) #porcentaje de 15%

total = precio - descuento

print("El total a pagar es: ", total)