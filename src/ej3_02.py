"""
Ejercicio 3.1.2

Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.
"""

from ej3_01 import pedirAsignaturas

def mensaje(asignaturas: list):

    for i in asignaturas:
        print("Yo estudio " + i)
    

def main():
    print("Introduce asignaturas (enter para terminar): ")
    mensaje(pedirAsignaturas())


if __name__ == "__main__":
    main()

