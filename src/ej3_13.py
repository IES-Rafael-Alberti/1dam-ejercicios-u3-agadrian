"""
Ejercicio 3.1.13

Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
"""


def pedirNumeros() -> list:
    """
    Pide por consola numeros hasta que introduce enter

    Retorna:
        numeros (list): lista de los numeros introducidos
    """
    ok = False
    numeros = []
    while not ok:
        try:
            numero = input("")
            if numero != "":
                numero = float(numero)
                numeros.append(numero)
            else:
                ok = True
                
        except:
            print("Error, debe introducir un valor numerico")

    return numeros



def calcularMedia(numeros: list) -> float:
    """
    Calcula la media de una lista de numeros

    Args:   
        numeros (list): lista de numeros de cualquier tipo

    Retorna:
            total (float): el valor de la media calculado
    """
    total = 0

    for i in numeros:
        total += i
    
    total = total / len(numeros)

    return total



def main():
    print("Introduce numeros (intro para parar): ")
    #print(pedirNumeros())

    print(calcularMedia(pedirNumeros()))



if __name__ == "__main__":
    main()