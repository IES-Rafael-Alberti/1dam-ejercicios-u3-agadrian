"""
Ejercicio 3.1.10

Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.
"""

def mayorMenorPrecio(precios: list):
    """
    Calcula el mayor y menor numero de una lista

    Args:
        precios (list): lista de precios

    Retorna:
            mayor: mayor numero
            menor: menor numero
    """
    precios.sort()
    mayor = precios[-1]
    menor = precios[0]

    return menor, mayor



def main():
    precios = [50, 75, 46, 22, 80, 65, 8]

    menor, mayor = mayorMenorPrecio(precios)

    print(f"Mayor precio: {mayor} \nMenor precio: {menor}")



if __name__ == "__main__":
    main()

