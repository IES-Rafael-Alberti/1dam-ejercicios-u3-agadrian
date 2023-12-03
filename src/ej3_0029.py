"""
Ejercicio 3.3.5

Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Crea un conjunto pares que contenga los números pares del conjunto numeros.
Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.
"""


def conjuntoPares(numeros:set) -> set:
    pares = []
    for i in numeros:
        if i % 2 == 0:
            pares.append(i)

    return set(pares)



def conjuntoMultiplo3(numeros:set) -> set:
    multiplos3 = []
    for i in numeros:
        if i % 3 == 0:
            multiplos3.append(i)

    return set(multiplos3)



def main():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    pares = conjuntoPares(numeros)
    print(f"Pares: {pares}")

    multiplos3 = conjuntoMultiplo3(numeros)
    print(f"Multiplos de 3: {multiplos3}")

    multiplos3Pares = pares & multiplos3
    print(f"Numeros comunes: {multiplos3Pares}")



if __name__ == "__main__":
    main()
