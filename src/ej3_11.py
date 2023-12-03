"""
Ejercicio 3.1.11

Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
"""


def productoEscalar(vector1: tuple, vector2: tuple) -> tuple:
    """
    Calcula el prodcuto escalar de dos vectores

    Args:
        vector1 (tuple)
        vector2 (tuple)
    
    Retorna:
        resultado (tuple): el vector resultante de la multiplicacion
    """
    resultado = tuple((vector1[i] * vector2[i]) for i in range(len(vector1)))
        
    return resultado



def main():
    vector1 = (1,2,3)
    vector2 = (-1,0,2)

    print(f"El producto escalar de {vector1} y {vector2} es: " + str(productoEscalar(vector1, vector2)))



if __name__ == "__main__":
    main()

