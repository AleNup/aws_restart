n = int(input("Cuántos ingresos vas a entrar?: "))

ingresos = []

for i in range(n):
    ing = int(input("Entre sus ingresos: ")) 
    ingresos.append(ing)

suma = 0

for i in ingresos:
    suma += ing

print("La suma de de los ingresos es:", suma)

