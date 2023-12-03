"""
Ejercicio 3.1.7

Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

# ord -> letras a numero ascii
# chr -> numero a letra
"""

def posicionMultiploTres(lista: list) -> list:
    """
    Copia la lista pasada como arg y le elimina los elementos que estan en una posicion multiplo de 3

    Args:
        lista (list): lista con valores
    
    Retorna:
            listaFinal (list): lista con los elementos deseados ya eliminados
    """
    listaFinal = lista.copy()

    for i in range(len(lista)):
        if i % 3 == 0:
            listaFinal.remove(lista[i]) 

    return listaFinal



def main():
    abecedario = list(chr(i) for i in range(ord("a"), ord("z") + 1))

    print(posicionMultiploTres(abecedario))
    


if __name__ == "__main__":
    main()