#Entrada: nombre y apellido
#Salida: Mensaje indicando las iniciales del nombre completo de la persona

name = input("Nombre: ")
apellido_paterno = input("Apellido Paterno: ")
apellido_materno = input("Apellido Materno: ")

print("Sus iniciales son: ", name[0] + apellido_paterno[0] + apellido_materno[0])
