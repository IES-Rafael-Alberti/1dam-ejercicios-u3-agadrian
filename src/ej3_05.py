"""
Ejercicio 3.1.5

Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""

from src.ej3_04 import mostrarListaFormateada


def crearLista(numero:int) -> list:
    """
    Crea una lista del 0 al numero pasado por argumento

    Args:
        numero: numero final de la lista

    Retorna:
            list: lista desde el 0 hasta el numero
    """
    lista = list(i for i in range(0,numero+1))

    return lista



def invertirLista(lista:list) -> list:
    """
    Invierte la lista pasada por parametro

    Args:
        lista: lista de valores

    Retorna:
            lista2: copia revertida de la lista original
    """
    lista2 = lista.copy()
    lista2.reverse()

    return lista2


def main():
    numeros = int(input("Introduce hasta que numero quieres la lista: "))
    lista = crearLista(numeros)
    lista2 = invertirLista(lista)

    print("Invirtiendo lista...")

    print("Lista introducida: " + mostrarListaFormateada(lista))
    print("Lista invertida: " + mostrarListaFormateada(lista2))


if __name__ == "__main__":
    main()