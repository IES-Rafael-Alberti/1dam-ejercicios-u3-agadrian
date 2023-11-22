"""
Ejercicio 3.3.4

Dadas las siguientes listas:

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.
"""

def crearConjunto(lista:list) -> set:
    return set(lista)



def main():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    set_frutas1 = crearConjunto(frutas1)
    set_frutas2 = crearConjunto(frutas2)

    # Interseccion de conjuntos
    frutas_comunes = set_frutas1 & set_frutas2
    print(f"Comunes: {frutas_comunes}")

    # Diferencia de conjuntos
    frutas_solo_en_frutas1 = set_frutas1 - set_frutas2
    print(f"Solo en frutas 1: {frutas_solo_en_frutas1}")

    frutas_solo_en_frutas2 = set_frutas2 - set_frutas1
    print(f"Solo en frutas 2: {frutas_solo_en_frutas2}")
    


if __name__ == "__main__":
    main()
