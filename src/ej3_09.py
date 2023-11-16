"""
Ejercicio 3.1.9

Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""

def pedirPalabra():
    """
    Pide palabra
    """

    palabra = input("Introduce palabra: ")

    return palabra.lower()


def contarVocales(palabra:str) -> tuple:
    """
    Almacena la cantidad de cada vocal que tiene una palabra

    Args:
        palabra (str): palabra deseada
    
    Retorna:
        vocales (tuple): una tupla que contiene la lista con el numero de veces que aparece cada vocal
    """
    vocales = (["a",0],["e",0],["i",0],["o",0],["u",0])

    for i in vocales:
        # El numero de cada letra = al numero de veces que haya esa letra en la palabra
        i[1] = palabra.count(i[0])

    return vocales



def main():
    print(contarVocales(pedirPalabra()))



if __name__ == "__main__":
    main()


