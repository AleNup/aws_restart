# La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)
#Input: Temperatura en Fahrenheit (float)
#Output: Temperatura en Celsius (float)

Fahrenheit = float(input("Ingrese una temperatura en Fahrenheit:  "))

Celsius = (5/9) * (Fahrenheit-32)

print("{} grados Fahrenheit son {} grados Celsius".format(Fahrenheit, Celsius))