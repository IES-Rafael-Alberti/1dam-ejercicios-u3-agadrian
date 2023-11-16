"""
Ejercicio 3.1.3

Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""


def pedirAsignaturas(numeroAsignaturas: int) -> list:
    """
    Almacena en una lista las asignaturas introducidas

    Args
        numeroAsignaturas (int): cantidad de asignatuas que tengo que introducir

    Retorna:
            list: asignaturas introducidas
    """

    return list(input("Introduce asignatura: ") for _ in range(numeroAsignaturas))



def asignarNota(asignaturas: list) -> list:
    """
    Pide la nota para cada asignatura y la almacena en una lista dentro de la lista principal

    Args:
        asignaturas (list): lista de asignaturas
    
    Retorna:
        asignaturas (list): lista que contiene varias listas de cada asignatura y su nota
    """
    for i in range(len(asignaturas)):
        nota = input("Introduce nota (" + asignaturas[i] + "): ")
        asignaturas[i] = list((asignaturas[i],nota))

    return asignaturas



def mostrarNotas(listaNotas: list):
    """
    Muestra la nota sacada en cada examen

    Args:
        listaNotas (List): lista de las asignaturas y su nota
    """
    for i in range(len(listaNotas)):
        print(f"En {listaNotas[i][0]} has sacado un {listaNotas[i][1]}")



def main():
    
    asignaturas = pedirAsignaturas(int(input("Cuantas asignaturas vas a introducir?: ")))
    
    asignaturasConNotas = asignarNota(asignaturas)
    
    mostrarNotas(asignaturasConNotas)



if __name__ == "__main__":
    main()