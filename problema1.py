#Input: Edad (entero >0), Año actual (entero >0)
#Output: Edad en el 2070 (entero >0)

age = int(input("Ingrese su edad: "))

year = int(input("Ingrese el año actual: "))

futureYear = (2070-year) + age

print(f"\nEl año actual es {year} y su edad es {age}")

print(f"\nSu edad en el 2070 será {futureYear} años")