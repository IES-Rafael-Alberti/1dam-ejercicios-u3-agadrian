"""
Ejercicio 3.3.6
Dado el conjunto de letras:

vocales = {'a', 'e', 'i', 'o', 'u'}
Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.
Estos ejercicios te ayudarán a practicar y comprender mejor cómo trabajar con conjuntos en Python. ¡Espero que te sean útiles! Si tienes alguna pregunta o necesitas más ejercicios, no dudes en decírmelo.
"""



def conjuntoConsonantes(letras:set, abecedario:list) -> set:
    
    consonantes = []
    for i in abecedario:
        if i not in letras:
            consonantes.append(i)

    return set(consonantes)




def main():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    abecedario = set(list(chr(i) for i in range(ord("a"), ord("z") + 1)))

    consonantes = abecedario - vocales
    print(f"Consonantes: {consonantes}")


if __name__ == "__main__":
    main()
