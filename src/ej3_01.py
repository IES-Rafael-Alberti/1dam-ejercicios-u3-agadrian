""""
Ejercicio 3.1.1

Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""

def pedirAsignaturas():
    asignaturas = []
    ok = False

    while not ok:
        asignatura = input("")
        if asignatura != "":
            asignaturas.append(asignatura)
        else:
            ok = True

    return asignaturas



def main():
    print("Introduce asignatura/s (enter para acabar): ")
    print(pedirAsignaturas())



if __name__ == "__main__":
    main()


