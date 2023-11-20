"""
Ejercicio 3.1.8

Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""

def pedirPalabra():
    palabra = input("Palabra a comprobar si es palindromo: ")
    palabra = list(palabra)

    return palabra



def comprobarPalindromo(palabra: dict) -> bool:
    """
    Comprueba si la palabra introducida es un palindromo

    Args: 
        palabra (str): palabra a comprobar

    Retorna:
            True: si es palindromo
            False: si no es palindromo
    """
    if palabra == palabra[::-1]:
        return True
    else:
        return False



def main():

    if comprobarPalindromo(pedirPalabra()):
        print("Es un palindromo")
    else:
        print("No es palindromo")



if __name__ == "__main__":
    main()


