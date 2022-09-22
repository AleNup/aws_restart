#Input: Kilómetros recorridos (float > 0), Litros de combustible gastados (float > 0)
#Output: Consumo por kilómetro.

m_recorridos = float(input ("Ingresa el valor de km recorridos:  "))
galones_combustible = float(input ("Ingresa el valor de galones consumidos: "))


total = (m_recorridos / galones_combustible)

print ("El consumo por kilometro es: ", total )