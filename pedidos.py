# Sistema de pedidos de un restaurante pequeño
# Version 1: productos disponibles, menu y datos del cliente
 
def pregunta_repeticiones():
    productosDisponibles = ["Hamburguesa", "Pizza", "Gaseosa"]
    preciosDisponibles = [12, 18, 4]
 
    cliente = input("Nombre del cliente: ")
    mesa = int(input("Numero de mesa: "))
 
    for i in range(0, len(productosDisponibles), 1):
        print(i + 1, productosDisponibles[i], "S/.", preciosDisponibles[i])
 
 
pregunta_repeticiones()
 
