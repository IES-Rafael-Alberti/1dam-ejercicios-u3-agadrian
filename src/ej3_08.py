"""
Ejercicio 3.1.8

Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""

def pedirPalabra():
    palabra = input("Palabra a comprobar si es palindromo: ")

    return palabra


def comprobarPalindromo(palabra):
    pass

def main():
    pass

if __name__ == "__main__":
    main()


pal = "ana"

if pal == pal[::-1]:
    print("si")
else:
    print("no")