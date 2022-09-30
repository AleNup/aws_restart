#Desarrollar un programa que muestre los primeros 10 números de la sucesión de
#Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada
#elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5,
#8, 13, 21, 34, 55…
#Ejemplo de ejecución:
#0
#1
#1
#2
#3
#5
#8
#13
#21
#34

'''
anterior = 0
actual = 1

print(anterior) # +1 numero de la sucesion

for i in range(9): #0,1,2,3,4,5,6,7,8,
    print(actual)
    auxiliar = actual #Se guarda el valor que se acaba de imprimir que sera el nuevo anterior
    actual = anterior + actual #operamos el siguiente actual
    anterior = auxiliar # asignamos el nuevo anterior
'''


def pintura():
    print("Necesitas el color rojo")

pintura()

def herramienta(x):
    print("Usa el pincel del mango" + x)

herramienta(" color marron")
