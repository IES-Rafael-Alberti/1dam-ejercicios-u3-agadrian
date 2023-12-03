"""
Ejercicio 3.2.3

Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	    Precio
Plátano	    1.35
Manzana 	0.80
Pera	    0.85
Naranja 	0.70
"""

def obtenerPrecio(frutas:dict, kilos, fruta):
    precioFinal = frutas[fruta] * kilos

    return precioFinal
    


def main():
    precioFrutas = {
        "platano": 1.35, 
        "manzana": 0.80, 
        "pera": 0.85, 
        "naranja": 0.70
        }
    
    fruta = input("Que fruta quieres: ")

    if fruta not in precioFrutas:
        print("No tenemos esa fruta")
    else:
        kilos = int(input("Cuantos kilos quieres de fruta?: "))
        print("Precio total: " + str(obtenerPrecio(precioFrutas, kilos, fruta)))
  


if __name__ == "__main__":
    main()